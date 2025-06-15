import math

from .base import UnaryOperation


class CosinusStrategy(UnaryOperation):
    symbols = ["cos"]

    def execute(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("CosinusStrategy expects a numeric input")
        radian = math.radians(a)
        return math.cos(radian)
