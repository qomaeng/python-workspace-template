from enum import auto, unique
from typing import TYPE_CHECKING, Any

from core.types import UpperStrEnum

from error.core import CoreError

if TYPE_CHECKING:
    from collections.abc import Mapping


@unique
class CommonErrorCodes(UpperStrEnum):
    UNKNOWN = auto()
    VALIDATION = auto()


class CommonError(CoreError):
    def __init__(
        self,
        message: str = "Common error",
        *,
        code: CommonErrorCodes,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=code, context=context)


class UnknownError(CommonError):
    def __init__(
        self,
        message: str = "Unknown error",
        *,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=CommonErrorCodes.UNKNOWN, context=context)


class ValidationError(CommonError):
    def __init__(
        self,
        message: str = "Validation failed",
        *,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message, code=CommonErrorCodes.VALIDATION, context=context)
