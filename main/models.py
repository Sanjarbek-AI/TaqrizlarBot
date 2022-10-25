import sqlalchemy
from sqlalchemy import DateTime

from main.constants import *
from main.database_set import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("city", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_address", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("district", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("birthdate", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("gender", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("married", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("telegram_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(UserStatus), nullable=True),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)
