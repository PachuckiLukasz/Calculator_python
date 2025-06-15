import math

from .base import UnaryOperation


class ArcSinusStrategy(UnaryOperation):
    symbols = ["arcsin"]

    def execute(self, a):
        if -1 > a or a > 1:
            raise ValueError("ArcSinusStrategy expects input in range (-1;1)")
        return math.asin(a)
