from typing import Annotated

from pydantic import BaseModel, Field

from core.common.common_types import AwareDatetime

from .types import UserId, UserName

__all__ = [
    "User",
]


class User(BaseModel):
    id: UserId
    created_at: AwareDatetime
    deleted_at: Annotated[AwareDatetime | None, Field(default=None)]

    name: UserName
