from strategies.base import Operation
import math


class RootStrategy(Operation):
    def execute(self, a, b):
        return a ** (1 / b)