import importlib

from strategies import *
from strategies.base import Operation, UnaryOperation
import os
strategy_dir = os.path.dirname(__file__)+"/strategies"
for fname in os.listdir(strategy_dir):
    if fname in os.listdir(strategy_dir):
        if fname.endswith(".py")and fname not in {"__init.py__", "base.py"}:
            module_name = "strategies." + fname[:-3]
            importlib.import_module(module_name)
strategy_map = {}

for cls in Operation.__subclasses__() + UnaryOperation.__subclasses__():
    if hasattr(cls, "symbols"):
        for sym in cls.symbols:
            strategy_map[sym] = cls()

if __name__ == "__main__":
    a = 3
    b = 4
    result = strategy_map['+'].execute(a, b)
    print("3 + 4 =", result)
