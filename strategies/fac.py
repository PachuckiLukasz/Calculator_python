import math
from .base import UnaryOperation


class FactorialStrategy(UnaryOperation):
    symbols = ["fac", "!"]

    def execute(self, a):
        if float(a).is_integer() and a >= 0:
            return math.factorial(int(a))
        raise ValueError("Liczba musi być całkowita i większa od 0")
