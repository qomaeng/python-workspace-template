from typing import TYPE_CHECKING, Annotated

from contract.common.schemas import ApiErrorResponse
from contract.user.response import SearchUserResponse
from fastapi import APIRouter, Query
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

if TYPE_CHECKING:
    from contract.user.request import SearchUserRequest

user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get(
    "/",
    summary="Search users",
    description="Search users with filters and pagination.",
    response_description="User search result",
    status_code=HTTP_200_OK,
    response_model=SearchUserResponse,
    responses={
        HTTP_400_BAD_REQUEST: {
            "model": ApiErrorResponse,
            "description": "Invalid search condition",
        },
        HTTP_404_NOT_FOUND: {
            "model": ApiErrorResponse,
            "description": "User not found",
        },
    },
)
async def search_users(
    request: Annotated[SearchUserRequest, Query()],
) -> SearchUserResponse:
    return SearchUserResponse()
