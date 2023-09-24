import typing as tp
from custom_logger.logger import logger

# Генератор - это итератор, который получаетсяв результате вызова функции, содержащей ключевое слово yield.

def countdown(n: int) -> tp.Iterator[int]:
    logger.info(f'Counting down from {n}')
    for i in range(n, 0, -1):
        yield i
    
    logger.info('Done')

counter = countdown(2)

logger.info(iter(counter) is counter)
try:
    for _ in range(3):
        logger.info(next(counter))
except StopIteration:
    logger.warning(f'Iteration finished, no more next values!')