from strategies.base import Operation


class DivStrategy(Operation):
    def execute(self, a, b):
        return a / b