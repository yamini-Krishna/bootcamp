
from types_module import ProcessorFn


# Define the to_uppercase processor
def to_uppercase(line: str) -> str:
    return line.upper()

# Define the to_snakecase processor
def to_snakecase(line: str) -> str:
    return line.replace(" ", "_").lower()
