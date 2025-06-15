import math
from strategies.base import UnaryOperation


class SqrtStrategy(UnaryOperation):
    symbols = ["sqrt"]

    def execute(self, a):
        if a < 0:
            raise ValueError("Nie można pierwiastkować liczby ujemnej")
        return math.sqrt(a)
