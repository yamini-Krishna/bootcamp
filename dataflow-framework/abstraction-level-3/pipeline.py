import yaml
import importlib
from typing import List
from types import ModuleType
from types import SimpleNamespace
from types import FunctionType
from types import ModuleType
from types import GeneratorType
from types import MethodType
from types import CodeType
from types import BuiltinFunctionType

from types import FunctionType
from types import ModuleType
from types import BuiltinFunctionType

from types import FunctionType
from types import ModuleType
from typing import Callable

ProcessorFn = Callable[[str], str]

def load_pipeline(config_path: str) -> List[ProcessorFn]:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    steps = config.get("pipeline", [])
    processors = []

    for step in steps:
        import_path = step["type"]
        module_path, func_name = import_path.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
            if not callable(func):
                raise TypeError(f"{func_name} is not callable")
            processors.append(func)
        except (ModuleNotFoundError, AttributeError, TypeError) as e:
            raise ImportError(f"Failed to load processor '{import_path}': {e}")

    return processors
