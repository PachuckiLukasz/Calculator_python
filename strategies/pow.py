from .base import Operation


class PowStrategy(Operation):
    symbols = ["^"]

    def execute(self, a, b):
        return a ** b
