from datetime import datetime

__all__ = [
    "is_aware",
    "is_naive",
]


def is_aware(d: datetime) -> bool:
    return d.tzinfo is not None


def is_naive(d: datetime) -> bool:
    return not is_aware(d)
