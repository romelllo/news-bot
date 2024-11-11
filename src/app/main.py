import logging

LOGGING_FORMAT = (
    "[%(asctime)s] [%(filename)s:%(lineno)d] | %(levelname)-8s | %(message)s"
)
logger = logging.getLogger()


def configure_logger() -> None:
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)


async def main() -> None:
    configure_logger()
    logger.info("Hello, World!")