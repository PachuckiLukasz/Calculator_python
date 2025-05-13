from strategies.base import Operation


class SubStrategy(Operation):
    def execute(self, a, b):
        return a - b