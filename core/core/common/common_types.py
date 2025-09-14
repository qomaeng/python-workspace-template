from enum import StrEnum
from typing import Annotated, Self

from pydantic import UUID4 as PydanticUUID4
from pydantic import UUID7 as PydanticUUID7
from pydantic import AwareDatetime as PydanticAwareDatetime
from pydantic import Field
from pydantic import NaiveDatetime as PydanticNaiveDatetime

from .common_constants import (
    INT32_MAX,
    INT32_MIN,
    INT64_MAX,
    INT64_MIN,
    UINT32_MAX,
    UINT32_MIN,
    UINT64_MAX,
    UINT64_MIN,
)

__all__ = [
    "Int32",
    "Int64",
    "UInt32",
    "UInt64",
    "ID32",
    "ID64",
    "UUID4",
    "UUID7",
    "AwareDatetime",
    "NaiveDatetime",
    "UpperStrEnum",
]

type Int32 = Annotated[int, Field(ge=INT32_MIN, le=INT32_MAX)]
type Int64 = Annotated[int, Field(ge=INT64_MIN, le=INT64_MAX)]

type UInt32 = Annotated[int, Field(ge=UINT32_MIN, le=UINT32_MAX)]
type UInt64 = Annotated[int, Field(ge=UINT64_MIN, le=UINT64_MAX)]

type ID32 = Annotated[int, Field(ge=1, le=INT32_MAX)]
type ID64 = Annotated[int, Field(ge=1, le=INT64_MAX)]

type UUID4 = PydanticUUID4
type UUID7 = PydanticUUID7

type AwareDatetime = PydanticAwareDatetime
type NaiveDatetime = PydanticNaiveDatetime


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
