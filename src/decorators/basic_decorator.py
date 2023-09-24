from custom_logger.logger import logger

def deco(func):
    def wrapper():
        logger.info("Wrapper func")

    return wrapper


@deco
def f():
    logger.info("f")


logger.info(f)
f()
