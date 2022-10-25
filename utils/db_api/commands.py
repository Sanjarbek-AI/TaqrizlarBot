from main.constants import UserStatus
from main.database_set import database
from main.models import users


async def get_user(telegram_id):
    try:
        query = users.select().where(users.c.telegram_id == telegram_id)
        return await database.fetch_one(query=query)
    except Exception as exc:
        print(exc)
        return False


# async def get_users():
#     try:
#         query = users.select().where(users.c.status == UserStatus.active)
#         return await database.fetch_all(query=query)
#     except Exception as exc:
#         print(exc)
#         return False
#

async def register(message, state):
    try:
        data = await state.get_data()
        query = users.insert().values(
            telegram_id=data.get("telegram_id"),
            full_name=data.get("full_name"),
            gender=data.get("gender"),
            birthdate=data.get("birthdate"),
            phone_number=data.get("phone_number"),
            married=data.get("status"),
            status=UserStatus.active,
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        print(exc)
        return False

#
# async def get_about():
#     try:
#         query = about.select()
#         return await database.fetch_all(query=query)
#     except Exception as exc:
#         print(exc)
#         return False
#
#
# async def add_about(message, state):
#     try:
#         data = await state.get_data()
#         query = about.insert().values(
#             text=data.get("text"),
#             created_at=message.date,
#             updated_at=message.date
#         )
#         await database.execute(query=query)
#         return True
#     except Exception as exc:
#         print(exc)
#         return False
