import math

from .base import UnaryOperation


class CoshStrategy(UnaryOperation):
    symbols = ["cosh"]

    def execute(self, a):
        return math.cosh(a)
