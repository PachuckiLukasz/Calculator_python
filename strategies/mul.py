from strategies.base import Operation


class MulStrategy(Operation):
    def execute(self, a, b):
        return a * b
