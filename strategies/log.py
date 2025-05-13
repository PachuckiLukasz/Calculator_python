from strategies.base import Operation
import math


class LogStrategy(Operation):
    def execute(self, a):
        return math.log10(a)
