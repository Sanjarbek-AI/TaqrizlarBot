from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


async def users_main_menu():
    user_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Taqrizlar ✍"),
                KeyboardButton(text="Kitob izlash 🔎")
            ],
            [
                KeyboardButton(text="Tafsiyalar 📚"),
                KeyboardButton(text="Do'konlar 🛖")
            ],
            [
                KeyboardButton(text="Skidkalar 🎁"),
                KeyboardButton(text="Tavsiya berish ⏏")
            ]

        ], resize_keyboard=True
    )
    return user_menu


async def contact_def():
    contact = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Telefon raqamni jo'natish 📞", request_contact=True)
            ]
        ], resize_keyboard=True
    )
    return contact


async def users_gender_menu():
    user_gender = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Erkak 🧔🏻‍♂"),
                KeyboardButton(text="Ayol 🧕🏻")
            ]
        ], resize_keyboard=True
    )
    return user_gender


async def users_status_menu():
    user_gender = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Ha ✅"),
                KeyboardButton(text="Yo'q ❌")
            ]
        ], resize_keyboard=True
    )
    return user_gender
