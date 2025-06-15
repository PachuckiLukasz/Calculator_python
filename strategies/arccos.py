import math

from .base import UnaryOperation


class ArcCosinusStrategy(UnaryOperation):
    symbols = ["arccos"]

    def execute(self, a):
        if a < -1 or a > 1:
            raise ValueError("ArcCosinusStrategy expects input in range [-1;1]")
        return math.acos(a)
