from custom_logger.logger import logger

b = 6

def f2(a) -> None:
    logger.info(a)
    logger.info(b)
    b = 9

if __name__ == "__main__":
    f2(3)
