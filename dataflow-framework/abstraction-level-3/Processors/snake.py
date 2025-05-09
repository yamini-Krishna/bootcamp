import re

def to_snakecase(line: str) -> str:
    words = re.findall(r'[a-zA-Z0-9]+', line)
    return '_'.join(word.lower() for word in words)
