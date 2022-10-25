from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    full_name = State()
    birthdate = State()
    gender = State()
    status = State()
    phone_number = State()
