from core.logging import setup_logger
from fastapi import FastAPI

from api_server.lifespan import lifespan
from api_server.user.router import user_router

setup_logger()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
