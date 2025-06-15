import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calculator import Calculator
from CalculatorController import CalculatorController


def test_exit_operation():
    calc = Calculator()
    calc.operator = "X"
    result = calc.perform_operation()
    assert result == "Koniec obliczeń"
    assert calc.keep_going == False


def test_addition():
    calc = Calculator()
    calc.first_num = 2
    calc.second_num = 3
    calc.operator = "A"
    result = calc.perform_operation()
    assert result == "2.0 + 3.0 = 5.0"


def test_subtraction():
    calc = Calculator()
    calc.first_num = 6
    calc.second_num = 3
    calc.operator = "S"
    result = calc.perform_operation()
    assert result == "6.0 - 3.0 = 3.0"


def test_multiply():
    calc = Calculator()
    calc.first_num = 3
    calc.second_num = 4
    calc.operator = "M"
    result = calc.perform_operation()

    assert result == "3.0 * 4.0 = 12.0"


def test_divide():
    calc = Calculator()
    calc.first_num = 6
    calc.second_num = 5
    calc.operator = "D"
    result = calc.perform_operation()
    assert result == "6.0 / 5.0 = 1.2"


def test_modulo():
    calc = Calculator()
    calc.first_num = 10
    calc.second_num = 3
    calc.operator = "MOD"
    result = calc.perform_operation()
    assert result == "10.0 % 3.0 = 1.0"


def test_modulo_by_zero():
    calc = Calculator()
    calc.first_num = 15
    calc.second_num = 0
    calc.operator = "MOD"
    result = calc.perform_operation()
    assert "Błąd - niedozwolone dane wejściowe dla %" in result


def test_power():
    calc = Calculator()
    calc.first_num = 3
    calc.second_num = 3
    calc.operator = "P"
    result = calc.perform_operation()
    assert result == "3.0 ^ 3.0 = 27.0"


def test_logarithm():
    calc = Calculator()
    calc.first_num = 1000
    calc.operator = "LOG"
    result = calc.perform_operation()
    assert result == "log10(1000.0) = 3.0"


def test_log_of_lower_than_zero():
    calc = Calculator()
    calc.first_num = -5
    calc.operator = "LOG"
    result = calc.perform_operation()
    assert "Błąd - niedozwolona wartość wejściowa dla log10" in result


def test_controller_negative_number_log():
    calc = Calculator()
    history = []
    calc_contr = CalculatorController(calc, history)
    result = calc_contr.parse("log(-1)")
    assert "Błąd" in result


def test_root():
    calc = Calculator()
    calc.first_num = 2
    calc.second_num = 9
    calc.operator = "R"
    result = calc.perform_operation()
    assert result == "2.0 √ 9.0 = 3.0"


def test_root_by_negative():
    calc = Calculator()
    calc.first_num = 2
    calc.second_num = -9
    calc.operator = "R"
    result = calc.perform_operation()
    assert "Wynik jest liczbą zespoloną" in result


def test_unknown_operator_returns_error_message():
    calc = Calculator()
    calc.first_num = 12
    calc.second_num = 4
    calc.operator = "J"
    result = calc.perform_operation()
    assert "Nieznana operacja." in result


def test_div_by_zero():
    calc = Calculator()
    calc.first_num = 15
    calc.second_num = 0
    calc.operator = "D"
    result = calc.perform_operation()
    assert "Błąd - dzielenie przez 0" in result


def test_controller_handles_division_by_zero():
    calc = Calculator()
    history = []
    calc_contr = CalculatorController(calc, history)
    result = calc_contr.parse("5/0")
    assert "Błąd - dzielenie przez 0" in result


def test_choose():
    calc = Calculator()
    calc.first_num = 5
    calc.second_num = 2
    calc.operator = 'C'
    result = calc.perform_operation()
    assert result == "5.0 nCk 2.0 = 10.0"


def test_perform_sin_operation():
    calc = Calculator()
    calc.operator = "SIN"
    calc.first_num = 90
    result = calc.perform_operation()
    assert result.lower().startswith("sin(90.0)") and "= 1.0" in result
