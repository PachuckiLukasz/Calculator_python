from strategies.base import Operation


class ModStrategy(Operation):
    def execute(self, a, b):
        return a % b