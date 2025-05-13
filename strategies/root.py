from strategies.base import Operation
import math


class RootStrategy(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Błąd: Nie możesz dzielić przez 0")
        if a < 0 and float(b).is_integer() and int(b) % 2 == 0:
            raise Exception("Błąd: Wynik jest liczbą zespoloną")
        return a ** (1 / b)
