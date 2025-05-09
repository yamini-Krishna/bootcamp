
from core import to_uppercase, to_snakecase
from types_module import ProcessorFn


def get_pipeline(mode: str) -> list[ProcessorFn]:
    """
    Based on the mode, return a list of processors.
    """
    if mode == "snakecase":
        return [to_snakecase]
    else:  # default mode is uppercase
        return [to_uppercase]
