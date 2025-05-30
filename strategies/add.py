from calc.strategies.base import Operation

class AddStrategy(Operation):
    def execute(self, a, b):
        return a+b