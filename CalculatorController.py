from operator_mapping import strategy_to_symbol, symbol_to_strategy


class CalculatorController:
    def __init__(self, calc, history):
        self.calc = calc
        self.history = history

    def parse(self, text):
        if text.lower().startswith("log"):
            try:
                self.calc.operator = "LOG"
                parts = text.split('(')
                self.calc.first_num = float(parts[1].removesuffix(')'))
                result = self.calc.perform_operation()
                formatted = f"Wynik: {result}"
                self.history.append(formatted)
                return formatted
            except Exception:
                return "Błąd - nieprawidłowe dane"
        elif text.lower().startswith("r("):
            return self.handle_root(text)
        elif "x" == text.lower():
            self.calc.operator = "X"
            result = self.calc.perform_operation()
            formatted = f"Wynik: Koniec obliczeń"
            self.history.append(formatted)
            return formatted
        operators = ['+', '-', '*', '/', '%', '^']
        return self.handle_binary_operation(operators, text)


    def handle_binary_operation(self, operators, text):
        for operator in operators:
            if operator in text:
                print("znaleziony operator: ", operator)
                try:
                    a_str, b_str = text.split(operator)
                    print("Lewa liczba:", a_str, "\nPrawa liczba:", b_str)
                    a = float(a_str)
                    b = float(b_str)
                    print("A float:", a, "\nB float:", b)
                    operation_name = symbol_to_strategy[operator]
                    self.calc.operator = strategy_to_symbol[operation_name]
                    self.calc.first_num = a
                    self.calc.second_num = b
                    result = self.calc.perform_operation()
                    print("Wynik:", result)
                    self.history.append(f"{text} = {result}")
                    return f"Wynik: {result}"
                except Exception:
                    return "Błąd - nieprawidłowe dane"
        return "Błąd - nieprawidłowe dane"

    def handle_root(self, text):
        try:
            self.calc.operator = "R"
            content = text[2:-1]
            degree_str, number_str = content.split(',')
            self.calc.first_num = float(degree_str)
            self.calc.second_num = float(number_str)
            result = self.calc.perform_operation()
            formatted = f"Wynik: {result}"
            self.history.append(formatted)
            return formatted
        except Exception:
            return "Błąd - nieprawidłowe dane"
