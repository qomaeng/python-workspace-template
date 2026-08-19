from enum import auto, unique
from typing import TYPE_CHECKING, Any

from core.common.errors import CoreError
from core.common.types import UpperStrEnum

if TYPE_CHECKING:
    from collections.abc import Mapping

__all__ = [
    "DeletedUserError",
    "DuplicateUserError",
    "NotFoundUserError",
    "UserError",
    "UserErrorCodes",
]


@unique
class UserErrorCodes(UpperStrEnum):
    NOT_FOUND_USER = auto()
    DUPLICATE_USER = auto()
    DELETED_USER = auto()


class UserError(CoreError):
    def __init__(
        self,
        message: str = "User error",
        *,
        code: UserErrorCodes,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=code, context=context)


class NotFoundUserError(UserError):
    def __init__(
        self,
        message: str = "Not found user",
        *,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=UserErrorCodes.NOT_FOUND_USER, context=context)


class DuplicateUserError(UserError):
    def __init__(
        self,
        message: str = "Duplicate user",
        *,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=UserErrorCodes.DUPLICATE_USER, context=context)


class DeletedUserError(UserError):
    def __init__(
        self,
        message: str = "Deleted user",
        *,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=UserErrorCodes.DELETED_USER, context=context)
