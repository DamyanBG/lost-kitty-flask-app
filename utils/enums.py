import enum


class RoleType(enum.Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"


class CatStatus(enum.Enum):
    lost = "lost"
    found = "found"
