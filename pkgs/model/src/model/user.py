from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime


@dataclass(slots=True, kw_only=True)
class User:
    id: str
    created_at: datetime
    deleted_at: datetime | None = None

    name: str
