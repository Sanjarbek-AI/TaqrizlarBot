from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from keyboards.default.admins import admin_main_menu
from keyboards.default.users import users_main_menu, contact_def, users_gender_menu, users_status_menu
from loader import dp, bot
from main import config
from states.users import Register
from utils.db_api.commands import get_user, register


@dp.message_handler(chat_id=config.ADMINS, commands="start")
async def start_admin(message: types.Message):
    text = "Assalomu alaykum. Siz bot boshqaruvchilaridan birisiz."
    await message.answer(text, reply_markup=await admin_main_menu())


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await get_user(message.chat.id)
    if user:
        text = "Assalomu alaykum. Botga xush kelebsiz."
        await message.answer(text, reply_markup=await users_main_menu())
    else:
        text = "Assalomu alaykum. Iltimos to'liq ismingizni kiriting."
        await Register.full_name.set()
        await message.answer(text)


@dp.message_handler(state=Register.full_name)
async def language(message: types.Message, state: FSMContext):
    await state.update_data({
        "full_name": message.text,
    })

    text = "Iltimos, telefon raqamingizni pastdagi tugmadan foydalangan holda kiriting."
    await Register.phone_number.set()
    await message.answer(text, reply_markup=await contact_def())


@dp.message_handler(state=Register.phone_number)
async def get_phone_number(message: types.Message):
    text = "Iltimos tugmadan foydalaning."
    await message.answer(text, reply_markup=await contact_def())


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=Register.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number
    })

    text = "Tug'ilgan sangizni kiriting. \nNamuna: 28.02.2002 \nkun : oy : yil"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await Register.birthdate.set()


@dp.message_handler(state=Register.birthdate)
async def language(message: types.Message, state: FSMContext):
    await state.update_data({
        "birthdate": message.text,
    })
    text = "Turmush qurganmisiz ?"
    await Register.status.set()

    await message.answer(text, reply_markup=await users_status_menu())


@dp.message_handler(state=Register.status)
async def language(message: types.Message, state: FSMContext):
    await state.update_data({
        "status": message.text,
    })
    text = "Iltimos, jinsingizni tasdiqlang !"
    await Register.gender.set()

    await message.answer(text, reply_markup=await users_gender_menu())


@dp.message_handler(state=Register.gender)
async def language(message: types.Message, state: FSMContext):
    await state.update_data({
        "gender": message.text,
        "telegram_id": message.chat.id,
    })
    registered_user = await register(message, state)
    message_admin = ""
    if registered_user:
        try:
            text = "✅ Siz muvofaqqiyatli ro'yxatdan o'tdingiz."
            message_admin = "✅ Ushbu foydalanuchi muvofaqqiyatli ro'yxatdan o'tdi."
            await message.answer(text, reply_markup=await users_main_menu())
        except Exception as exc:
            print(exc)

    else:
        text = "✅ Siz muvofaqqiyatli ro'yxatdan o'tdingiz."
        await message.answer(text, reply_markup=await users_main_menu())

        message_admin = "❌ Ushbu foydalanuchi ro'yxatdan o'ta olmadi. Botda muommo bor.\n\n"
    data = await state.get_data()
    message_admin += f"""\n
FI: {data.get("full_name")} \n
Gender: {data.get("gender")} \n
Birthdate: {data.get("birthdate")} \n
Married: {data.get("status")} \n
Phone number: {data.get("phone_number")}
"""
    await bot.send_message(chat_id="1358470521", text=message_admin)
    await state.finish()
