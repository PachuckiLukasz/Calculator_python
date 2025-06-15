import math

from .base import UnaryOperation


class SinusStrategy(UnaryOperation):
    symbols = ["sin"]

    def execute(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("SinusStrategy expects a numeric input")
        radian = math.radians(a)
        return math.sin(radian)
