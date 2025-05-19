import logging

def setup_logger(name: str, level: str = "INFO"):
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(getattr(logging, level.upper(), logging.INFO))

        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, level.upper(), logging.INFO))

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return logger
