from calc.strategies.base import Operation


class ModStrategy(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Błąd: Nie możesz dzielić przez 0")
        return a % b