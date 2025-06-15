import pytest

from rpn_evaluator import tokenize
from rpn_evaluator import shunting_yard
from rpn_evaluator import evaluate_rpn_with_strategies


def test_tokenize_log_expression():
    expr = "log(100) + 3^2"
    expected = ["log", "(", "100", ")", "+", "3", "^", "2"]
    result = tokenize(expr)
    assert result == expected


def test_tokenize_sqrt_expression():
    expr = "5 + sqrt(2^2 + 3^2)"
    expected = ["5", "+", "sqrt", "(", "2", "^", "2", "+", "3", "^", "2", ")"]
    result = tokenize(expr)
    assert result == expected


def test_tokenize_handles_comma_separated_arguments():
    expr = "r(3, 27)"
    expected = ["r", "(", "3", ",", "27", ")"]
    result = tokenize(expr)
    assert result == expected


def test_shunting_yard_root_function():
    tokens = ["r", "(", "3", ",", "27", ")"]
    expected = [3.0, 27.0, "r"]
    result = shunting_yard(tokens)
    assert result == expected


def test_evaluate_rpn_handles_nested_operations_with_unary_and_binary_strategies():
    tokens = [2.0, 2.0, "^", 3.0, 2.0, "^", "+", "sqrt"]
    result = evaluate_rpn_with_strategies(tokens)
    assert result == pytest.approx(3.605551275463989)


def test_evaluate_rpn_raises_on_unknown_token():
    tokens = [3.0, 4.0, "$"]
    with pytest.raises(ValueError) as exc_info:
        result = evaluate_rpn_with_strategies(tokens)
    assert "Nieznany token" in str(exc_info.value)


def test_evaluate_rpn_raises_on_division_by_zero():
    tokens = [3.0, 0.0, "/"]
    with pytest.raises(ZeroDivisionError) as exc_info:
        result = evaluate_rpn_with_strategies(tokens)
    assert "Błąd: Nie możesz dzielić przez 0" in str(exc_info.value)

