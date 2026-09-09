from logging.config import dictConfig
from pathlib import Path


def setup_logger(level: str = "INFO", *, log_file: str = "logs/app.log") -> None:
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(name)s:%(filename)s:%(lineno)d: %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                },
                "file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "default",
                    "filename": str(log_path),
                    "encoding": "utf-8",
                    "interval": 1,
                    "backupCount": 30,
                    "utc": False,
                },
            },
            "root": {
                "level": level,
                "handlers": ["console", "file"],
            },
            "loggers": {
                "uvicorn.access": {
                    "level": level,
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
                "uvicorn.error": {
                    "level": level,
                    "handlers": ["console", "file"],
                    "propagate": False,
                },
            },
        }
    )
