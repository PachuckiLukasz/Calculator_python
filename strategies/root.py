from .base import Operation


class RootStrategy(Operation):
    symbols = ["r"]

    def execute(self, a, b):
        if a == 0:
            raise ZeroDivisionError("Pierwiastek zerowego stopnia nie istnieje")
        if b < 0 and float(a).is_integer() and int(a) % 2 == 0:
            raise ValueError("Wynik jest liczbą zespoloną")
        if b < 0 and int(a) % 2 == 1:
            return -((-b) ** (1 / a))

        return b ** (1 / a)
