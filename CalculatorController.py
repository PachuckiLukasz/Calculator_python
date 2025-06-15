from operator_mapping import strategy_to_symbol, symbol_to_strategy


class CalculatorController:
    def __init__(self, calc, history):
        self.calc = calc
        self.history = history

    def parse(self, text):
        text = text.lower()

        if text == "x":
            self.calc.operator = "X"
            self.calc.perform_operation()
            formatted = "Wynik: Koniec obliczeń"
            self.history.append(formatted)
            return formatted

        if text.startswith("r("):
            return self.handle_root(text)

        unary_keywords = {
            "log": "log",
            "sin": "sin",
            "cos": "cos",
            "tan": "tan",
            "cot": "cot",
            "!": "!",
        }

        for key, op in unary_keywords.items():
            try:
                if key == "!" and text.startswith("!(") and text.endswith(")"):
                    value = float(text[2:-1])
                elif text.startswith(f"{key}(") and text.endswith(")"):
                    value = float(text[len(key) + 1:-1])
                else:
                    continue

                self.calc.first_num = value
                self.calc.operator = op

                result = self.calc.perform_operation()
                if isinstance(result, (int, float)):
                    symbol = self.calc.SYMBOLS.get(op.upper(), op)
                    formatted = f"Wynik: {symbol}({value:.1f}) = {result:.1f}"
                else:
                    formatted = f"Wynik: {result}"
                self.history.append(formatted)
                return formatted

            except Exception as e:
                if isinstance(e, ValueError):
                    formatted = "Błąd - nieprawidłowe dane (np. tekst zamiast liczby)"
                elif isinstance(e, IndexError):
                    formatted = "Błąd - brak nawiasu lub niepełny zapis"
                else:
                    formatted = f"Błąd SYSTEMOWY: {type(e).__name__}: {e}"
                self.history.append(formatted)
                return formatted

        operators = ['+', '-', '*', '/', '%', '^']
        return self.handle_binary_operation(operators, text)

    def handle_binary_operation(self, operators, text):
        for operator in operators:
            if operator in text:
                try:
                    a_str, b_str = text.split(operator)

                    if not a_str.strip() or not b_str.strip():
                        return "Błąd - nieprawidłowy format (np. brak drugiej liczby)"

                    a = float(a_str)
                    b = float(b_str)

                    strategy_class = symbol_to_strategy.get(operator.lower())
                    if not strategy_class:
                        return "Błąd - nieznany operator"

                    strategy_name = strategy_class.__module__.split('.')[-1]
                    self.calc.operator = strategy_to_symbol[strategy_name]
                    self.calc.first_num = a
                    self.calc.second_num = b
                    result = self.calc.perform_operation()
                    self.history.append(f"{text} = {result}")
                    return f"Wynik: {result}"

                except Exception as e:
                    if isinstance(e, ValueError):
                        return "Błąd - nieprawidłowe dane (wartość liczby)"
                    elif isinstance(e, IndexError):
                        return "Błąd - nieprawidłowy format (np. brak drugiej liczby)"
                    return f"Błąd SYSTEMOWY: {type(e).__name__}: {e}"

        return "Błąd - nieznany operator"


    def handle_root(self, text):
        try:
            self.calc.operator = "R"
            content = text[2:-1]
            degree_str, number_str = content.split(',')

            degree = float(degree_str)
            value = float(number_str)

            self.calc.first_num = degree
            self.calc.second_num = value

            result = self.calc.perform_operation()
            formatted = f"Wynik: {result}"
            self.history.append(formatted)
            return formatted
        except Exception as e:
            if isinstance(e, ValueError):
                return "Błąd - nieprawidłowe dane (liczby)"
            elif isinstance(e, IndexError):
                return "Błąd - zły format, brak przecinka"
            return f"Błąd SYSTEMOWY: {type(e).__name__}: {e}"
