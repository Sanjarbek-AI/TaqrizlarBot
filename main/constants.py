from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class UserGender(str, Enum):
    male = "male"
    female = "female"
