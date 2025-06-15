import math

from .base import UnaryOperation


class CotangensStrategy(UnaryOperation):
    symbols = ["cot"]

    def execute(self, a):
        if not isinstance(a, (int, float)):
            raise TypeError("CotangentStrategy expects a numeric input")
        radian = math.radians(a)
        tan_val = math.tan(radian)
        if abs(tan_val) < 1e-10:
            raise ZeroDivisionError("Cotangent undefied for this degree")
        return 1 / tan_val
