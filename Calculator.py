from math_core import compute, compute_unary, single_arg_operations


class Calculator:
    SYMBOLS = {
        "A": "+",
        "S": "-",
        "M": "*",
        "P": "^",
        "D": "/",
        "MOD": "%",
        "R": "√",
        "LOG": "log10",
        "C": "nCk",
    }

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
        if self.operator in single_arg_operations:
            return self.perform_unary_operation()
        if self.operator in self.SYMBOLS:
            return self.perform_binary_operation()
        elif self.operator == "X":
            self.keep_going = False
            return "Koniec obliczeń"
        else:
            return "Nieznana operacja."

    def perform_unary_operation(self):
        try:
            result = compute_unary(self.first_num, self.operator)
            symbol = self.SYMBOLS[self.operator]
            return f"{symbol}({self.first_num:.1f}) = {result:.1f}"
        except ValueError as e:
            return f"Błąd - {e}"
        except Exception:
            return "Błąd: Wynik jest liczbą zespoloną"

    def perform_binary_operation(self):
        symbol = self.SYMBOLS[self.operator]
        try:
            return self.format_result(self.first_num, self.second_num, symbol, self.operator)
        except ZeroDivisionError:
            if self.operator in ("D", "MOD"):
                return "Błąd - dzielenie przez 0"
            elif self.operator == "R":
                return "Błąd - pierwiastkowanie przez 0"
            else:
                return "Błąd arytmetyczny"
        except OverflowError:
            return "Błąd - wynik zbyt duży"
        except Exception as e:
            return f"Błąd: {e}"

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
              "P - power \nLOG - logarithm\nR - root\nC - Choose \nX - stop")
        self.operator = input().upper()
        return self.operator
