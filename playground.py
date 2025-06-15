from strategies import *
from strategies.base import Operation, UnaryOperation

print(Operation.__subclasses__())
print(UnaryOperation.__subclasses__())

strategy_map = {}
for cls in Operation.__subclasses__() + UnaryOperation.__subclasses__():
    if hasattr(cls, "symbols"):
        for sym in cls.symbols:
            strategy_map[sym] = cls()

print(strategy_map["*"].execute(3,4))