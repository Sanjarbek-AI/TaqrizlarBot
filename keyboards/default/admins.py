from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


async def admin_main_menu():
    admin_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Odam qo'shish ➕"),
                KeyboardButton(text="Odam izlash 🔎")
            ],
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
                KeyboardButton(text="Maslahatlar 🥸")
            ],

        ], resize_keyboard=True
    )
    return admin_menu
