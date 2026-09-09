import asyncio
from logging import getLogger

from core.logging import setup_logger

setup_logger()

logger = getLogger(__name__)


async def main() -> None:
    logger.info("Hello World")


if __name__ == "__main__":
    asyncio.run(main())
