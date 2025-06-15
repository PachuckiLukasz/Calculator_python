import math

from .base import UnaryOperation


class TanhStrategy(UnaryOperation):
    symbols = ["tanh"]

    def execute(self, a):
        return math.tanh(a)
