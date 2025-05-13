from math_core import compute
from math_core import compute_single_argument


class Calculator:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0
        self.operator = ""
        self.keep_going = True

    def get_input(self):
        self.input_operator()
        if self.operator == "X":
            return
        self.first_num = self.input_number("Pierwsza liczba: ")
        if self.operator != "LOG":
            self.second_num = self.input_number("Druga liczba: ")

    def perform_operation(self):
        symbols = {
            "A": "+",
            "S": "-",
            "M": "*",
            "P": "^",
            "D": "/",
            "MOD": "%",
            "R": "√",
            "LOG": "log₁₀",
        }
        if self.operator == "LOG":
            try:
                result = compute_single_argument(self.first_num, self.operator)
                return f"log10({self.first_num:.1f}) = {result:.1f}"
            except ValueError:
                return "Błąd - liczba musi być większa od zera"
            except Exception:
                return "Błąd: Wynik jest liczbą zespoloną"
        if self.operator in symbols:
            symbol = symbols[self.operator]
            if self.operator in ("R", "D", "MOD"):
                try:
                    return self.format_result(self.first_num, self.second_num, symbol, self.operator)
                except ZeroDivisionError:
                    return "Błąd - dzielenie przez 0" if self.operator in (
                        "D", "MOD") else "Błąd - pierwiastkowanie przez 0"
                except Exception:
                    return "Błąd: Wynik jest liczbą zespoloną"
            else:
                return self.format_result(self.first_num, self.second_num, symbol, self.operator)
        elif self.operator == "X":
            self.keep_going = False
            return "Koniec obliczeń"
        else:
            return "Nieznana operacja."

    def format_result(self, a, b, symbol, operator):
        result = compute(a, b, operator)
        return f"{a:.1f} {symbol} {b:.1f} = {result:.1f}"

    def input_number(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                break
            except ValueError:
                print("To nie była liczba - spróbuj jeszcze raz ")
        return value

    def input_operator(self):
        print("Operation: \nA - add \nS - subtract \nM - multiply \nD - divide\nMOD - modulo\n"
              "P - power \nLOG - logarithm\nR - root \nX - stop")
        self.operator = input().upper()
        return self.operator
