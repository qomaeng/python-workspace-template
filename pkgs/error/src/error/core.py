from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Mapping


class CoreError(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: str,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.context = context

    def __str__(self) -> str:
        context = f"; context={self.context}" if self.context else ""

        return f"{self.code}: {self.message}{context}"
