from custom_logger.logger import logger
# iterable - это объект у которого определён метод iter,возвращающий итератор. Примеры: list, dict, range

# iterator - это объект у которого определён метод next. 
# Метод next при каждом вызове возвращает следующий элемент последовательности или выкидывает исключение StopIteration.


lst = [1, 2, 3]
it = lst.__iter__()
logger.info(it)

try:
    for _ in range(len(lst) + 1):
        logger.info(it.__next__())
except StopIteration:
    logger.warning(f'Iteration finished, no more next values!')

# --------------------------------------------------------
# lst = [1, 2, 3]
# it = iter(lst)
# try:
#     for _ in range(len(lst) + 1):
#         logger.info(next(it))
# except StopIteration:
#     logger.warning(f'Iteration finished, no more next values!')

# --------------------------------------------------------
