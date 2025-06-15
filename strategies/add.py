from .base import Operation


class AddStrategy(Operation):
    symbols = ["+"]

    def execute(self, a, b):
        return a + b
