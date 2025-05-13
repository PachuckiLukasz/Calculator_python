from strategies.base import UnaryOperation
import math


class LogStrategy(UnaryOperation):
    def execute(self, a):
        if a > 0:
            return math.log10(a)
        raise ValueError("Błąd: liczba musi być większa od zera")
