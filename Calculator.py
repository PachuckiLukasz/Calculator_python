from math_core import compute, compute_unary, single_arg_operations, operations
from operator_mapping import symbol_to_strategy, strategy_to_symbol


class Calculator:
    SYMBOLS = {
        "a": "+",
        "s": "-",
        "m": "*",
        "p": "^",
        "d": "/",
        "mod": "%",
        "r": "√",
        "log": "log10",
        "c": "nCk",
        "fac": "!",
        "!": "!",
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "cot": "cot",
        "arcsin": "arcsin",
        "arccos": "arccos",
        "arctan": "arctan",
        "sinh": "sinh",
        "cosh": "cosh",
        "tanh": "tanh",
    }

    VALIDATORS = {
        "arcsin": lambda x: -1 <= x <= 1,
        "arccos": lambda x: -1 <= x <= 1,
        "log": lambda x: x > 0,
        "fac": lambda x: x >= 0 and float(x).is_integer(),
    }

    BINARY_VALIDATORS = {
        "mod": lambda x, y: y != 0,
        "c": lambda x, y: x >= 0 and 0 <= y <= x
    }

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, str):
            self._operator = value.lower()
        else:
            self._operator = value

    def __init__(self):
        self.first_num = 0
        self.second_num = 0
        self._operator = ""
        self.keep_going = True
        self.history = []

    def get_input(self):
        self.input_operator()
        if self.operator == "x":
            return
        self.first_num = self.input_number("Pierwsza liczba: ")
        if self.operator not in single_arg_operations:
            self.second_num = self.input_number("Druga liczba: ")

    def perform_operation(self):
        if self.operator in single_arg_operations:
            return self.perform_unary_operation()
        if self.operator in self.SYMBOLS:
            return self.perform_binary_operation()
        elif self.operator == "x":
            self.keep_going = False
            return "Koniec obliczeń"
        else:
            return "Nieznana operacja."

    def perform_unary_operation(self):
        try:
            if not self.is_valid_input(self.first_num):
                return f"Błąd - niedozwolona wartość wejściowa dla {self.SYMBOLS.get(self.operator, self.operator)}"
            result = compute_unary(self.first_num, self.operator)
            symbol = self.SYMBOLS[self.operator]
            formatted = f"{symbol}({self.first_num:.1f}) = {result:.1f}"
            self.history.append(formatted)
            self.history = self.history[-10:]
            return formatted
        except ValueError as e:
            if "math domain error" in str(e):
                return "Błąd - wynik jest liczbą zespoloną"
            return f"Błąd - {e}"
        except Exception as e:
            return f"Błąd SYSTEMOWY: {type(e).__name__}: {e}"

    def perform_binary_operation(self):
        symbol = self.SYMBOLS[self.operator]
        try:
            if not self.is_valid_binary_input(self.first_num, self.second_num):
                return f"Błąd - niedozwolone dane wejściowe dla {symbol}"
            formatted = self.format_result(self.first_num, self.second_num, symbol, self.operator)
            self.history.append(formatted)
            self.history = self.history[-10:]
            return formatted
        except ZeroDivisionError:
            return "Błąd - dzielenie przez 0"
        except OverflowError:
            return "Błąd - wynik zbyt duży"
        except ValueError as e:
            if "math domain error" in str(e):
                return "Błąd - wynik jest liczbą zespoloną"
            return f"Błąd - {e}"
        except Exception as e:
            return f"Błąd SYSTEMOWY: {type(e).__name__}: {e}"

    def format_result(self, a, b, symbol, operator):
        result = compute(a, b, operator)
        if operator == "r":
            return f"{a:.1f} {symbol} {b:.1f} = {result:.1f}"
        else:
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
        print("Dostępne operacje dwuargumentowe:")
        for symbol in self.SYMBOLS:
            if symbol in operations:
                print(f"  {symbol:<6} - {self.SYMBOLS[symbol]}")

        print("\nDostępne operacje jednoargumentowe:")
        for symbol in self.SYMBOLS:
            if symbol in single_arg_operations:
                print(f"  {symbol:<6} - {self.SYMBOLS[symbol]}")

        print("\nX - zakończ")

        while True:
            raw = input("\nWybierz operator: ").strip()
            if raw.isalpha():
                raw = raw.lower()

            if raw == "x":
                self.operator = "x"
                return self.operator
            if raw.lower() == "h":
                if not self.history:
                    print("Brak historii")
                else:
                    for line in self.history:
                        print(line)
                continue
            mapped_strategy = symbol_to_strategy.get(raw)
            if mapped_strategy:
                symbol_key = mapped_strategy.__module__.split('.')[-1]
                self.operator = strategy_to_symbol[symbol_key].lower()
                return self.operator
            else:
                print("Nieznana operacja. Spróbuj ponownie.")

    def is_valid_input(self, x):
        validator = Calculator.VALIDATORS.get(self.operator)
        return validator(x) if validator else True

    def is_valid_binary_input(self, x, y):
        validator = Calculator.BINARY_VALIDATORS.get(self.operator)
        return validator(x, y) if validator else True
