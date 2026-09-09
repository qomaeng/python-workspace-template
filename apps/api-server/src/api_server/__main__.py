import uvicorn

from api_server.config import Config


def main() -> None:
    config = Config()  # pyright: ignore[reportCallIssue]

    uvicorn.run(
        "api_server.app:app",
        host=str(config.api_server.host),
        port=config.api_server.port,
        reload=False,
    )


if __name__ == "__main__":
    main()
