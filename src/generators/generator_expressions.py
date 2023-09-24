from custom_logger.logger import logger

for tshirt in (f'{c} {s}' for c in ["black", "white"] for s in ["S", "M", "L"]):
    logger.info(tshirt)
