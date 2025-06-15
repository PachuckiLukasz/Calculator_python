import math

from .base import UnaryOperation


class SinhStrategy(UnaryOperation):
    symbols = ["sinh"]

    def execute(self, a):
        return math.sinh(a)
