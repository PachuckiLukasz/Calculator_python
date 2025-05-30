from calc.strategies.base import Operation


class PowStrategy(Operation):
    def execute(self, a, b):
        return a ** b
