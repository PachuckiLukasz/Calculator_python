from .base import Operation
import math


class ChooseStrategy(Operation):
    symbols = ["choose", "c"]

    def execute(self, a, b):
        a = int(a)
        b = int(b)
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Błąd: musisz użyć liczb całkowitych")
        if not (0 <= b <= a):
            raise ValueError("Błąd: zakres musi się zawierać w 0 <= b <= a")
        return math.factorial(a) // (math.factorial(b) * (math.factorial(a - b)))
