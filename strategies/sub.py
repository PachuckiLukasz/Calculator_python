from .base import Operation


class SubStrategy(Operation):
    symbols = ["-"]

    def execute(self, a, b):
        return a - b
