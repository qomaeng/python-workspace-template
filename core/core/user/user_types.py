from typing import Annotated

from pydantic import Field

from core.common.common_types import ID64
from core.user.user_constants import USER_NAME_MAX_LENGTH, USER_NAME_MIN_LENGTH

__all__ = [
    "UserId",
    "UserName",
]

type UserId = ID64
type UserName = Annotated[
    str,
    Field(
        min_length=USER_NAME_MIN_LENGTH,
        max_length=USER_NAME_MAX_LENGTH,
    ),
]
