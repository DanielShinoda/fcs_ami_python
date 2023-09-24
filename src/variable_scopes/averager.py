from custom_logger.logger import logger

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
logger.info(avg(10))
logger.info(avg(1))
logger.info(avg(12))

logger.info(avg.__code__.co_varnames)
logger.info(avg.__code__.co_freevars)
logger.info(avg.__closure__[0].cell_contents)
