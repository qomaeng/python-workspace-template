from typing import Annotated

from pydantic import BaseModel, Field


class SearchUserRequest(BaseModel):
    name: str | None = None
    include_deleted: bool = False

    limit: Annotated[int, Field(ge=1, le=100)] = 20
    offset: Annotated[int, Field(ge=0)] = 0
