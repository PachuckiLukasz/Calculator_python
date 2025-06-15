from .base import UnaryOperation

import math


class LogStrategy(UnaryOperation):
    symbols = ["log"]

    def execute(self, a):
        if a > 0:
            return math.log10(a)
        raise ValueError("liczba musi być większa od zera")
