from collections.abc import Mapping
from enum import auto, unique
from typing import Any

from .common_types import UpperStrEnum

__all__ = [
    "CoreError",
    "CommonErrorCodes",
    "CommonError",
    "UnknownError",
    "ValidationError",
]


class CoreError(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: str,
        context: Mapping[str, Any] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.code = code
        self.context = context

    def __str__(self) -> str:
        context = f"; context={self.context}" if self.context else ""
        return f"{self.code}: {self.message}{context}"


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
    ):
        super().__init__(message, code=code, context=context)


class UnknownError(CommonError):
    def __init__(
        self,
        message: str = "Unknown error",
        *,
        context: Mapping[str, Any] | None = None,
    ):
        super().__init__(message, code=CommonErrorCodes.UNKNOWN, context=context)


class ValidationError(CommonError):
    def __init__(
        self,
        message: str = "Validation failed",
        *,
        context: Mapping[str, Any] | None = None,
    ):
        super().__init__(message, code=CommonErrorCodes.VALIDATION, context=context)
