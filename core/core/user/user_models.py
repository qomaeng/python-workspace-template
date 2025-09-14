from pydantic import BaseModel

from core.common.common_types import AwareDatetime

from .user_types import UserId, UserName

__all__ = [
    "User",
]


class User(BaseModel):
    id: UserId
    created_at: AwareDatetime
    deleted_at: AwareDatetime | None

    name: UserName
