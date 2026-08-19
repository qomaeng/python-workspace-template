from typing import Any

from core.logging import setup_logger
from fastapi import FastAPI

setup_logger()

app = FastAPI()


@app.get("/")
def root() -> dict[str, Any]:
    return {"Hello": "World"}
