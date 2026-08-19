from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from core.common.types import AwareDatetime

    from .types import UserId, UserName

__all__ = [
    "User",
]


class User(BaseModel):
    id: UserId
    created_at: AwareDatetime
    deleted_at: Annotated[AwareDatetime | None, Field(default=None)]

    name: UserName
