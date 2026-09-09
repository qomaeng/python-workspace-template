from enum import StrEnum
from typing import Self


class UpperStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(
        name: str,
        start: int,
        count: int,
        last_values: list[str],
    ) -> str:
        return name.upper()

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        value = value.upper() if isinstance(value, str) else str(value).upper()
        for member in cls:
            if member.value == value:
                return member

        return None
