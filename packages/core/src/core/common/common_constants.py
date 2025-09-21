__all__ = [
    "INT32_MIN",
    "INT32_MAX",
    "INT64_MIN",
    "INT64_MAX",
    "UINT32_MIN",
    "UINT32_MAX",
    "UINT64_MIN",
    "UINT64_MAX",
]

INT32_MIN: int = -(2 ** (32 - 1))
INT32_MAX: int = 2 ** (32 - 1) - 1
INT64_MIN: int = -(2 ** (64 - 1))
INT64_MAX: int = 2 ** (64 - 1) - 1

UINT32_MIN: int = 0
UINT32_MAX: int = 2**32 - 1
UINT64_MIN: int = 0
UINT64_MAX: int = 2**64 - 1
