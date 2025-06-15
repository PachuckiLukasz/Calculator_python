from .base import Operation


class MulStrategy(Operation):
    symbols = ["*"]

    def execute(self, a, b):
        return a * b
