import math

from .base import UnaryOperation


class TangensStrategy(UnaryOperation):
    symbols = ["tan"]

    def execute(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("TangentStrategy expects a numeric input")
        radian = math.radians(a)
        return math.tan(radian)
