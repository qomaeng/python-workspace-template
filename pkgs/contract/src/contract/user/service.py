from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from contract.user.request import SearchUserRequest
    from contract.user.response import SearchUserResponse


class UserService(Protocol):
    async def search_users(self, request: SearchUserRequest) -> SearchUserResponse: ...
