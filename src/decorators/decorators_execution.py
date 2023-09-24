from custom_logger.logger import logger

registry: list = list()


def register(func):
    logger.info(f"Running register({func})")
    registry.append(func)
    return func


@register
def f1():
    logger.info("Running f1()")


@register
def f2():
    logger.info("Running f2()")


def f3():
    logger.info("Running f3()")


def main():
    logger.info("Running main!")
    logger.info(f"Registry -> {registry}")
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
