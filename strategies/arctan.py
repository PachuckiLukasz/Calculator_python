import math

from .base import UnaryOperation


class ArcTangensStrategy(UnaryOperation):
    symbols = ["arctan"]

    def execute(self, a):
        return math.atan(a)
