from calc.strategies.base import Operation
import math


class LogStrategy(UnaryOperation):
    def execute(self, a):
        if a > 0:
            return math.log10(a)
        raise ValueError("liczba musi być większa od zera")
