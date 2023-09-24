from custom_logger.logger import logger


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
logger.info(avg(10))
logger.info(avg(1))
logger.info(avg(12))

logger.info(f"Local variables of a function: {avg.__code__.co_varnames}")
logger.info(f"Closure variables of a function: {avg.__code__.co_freevars}")
logger.info(
    f"Count value of a function: {avg.__closure__[0].cell_contents}, \
    total value of a function: {avg.__closure__[1].cell_contents}"
)
