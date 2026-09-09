from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from api_server.config import Config

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from fastapi import FastAPI, Request


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.config = Config()  # pyright: ignore[reportCallIssue]

    yield


def depends_config(request: Request) -> Config:
    return request.app.state.config
