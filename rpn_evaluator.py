import strategies.base
from rpn_strategy_map import strategy_map
from strategies.base import Operation, UnaryOperation
import re


def evaluate_rpn_with_strategies(rpn_tokens):
    stack = []

    for token in rpn_tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in strategy_map:
            strategy = strategy_map[token]
            if isinstance(strategy, Operation):
                b = stack.pop()
                a = stack.pop()
                result = strategy.execute(a, b)
                stack.append(result)
            elif isinstance(strategy, UnaryOperation):
                a = stack.pop()
                result = strategy.execute(a)
                stack.append(result)
            else:
                raise ValueError(f"Nieznany token: {token}")
        else:
            raise ValueError(f"Nieznany token: {token}")
    if len(stack) != 1:
        raise ValueError("Niewłaściwa liczba elementów na stosie po ewaluacji")
    else:
        return stack.pop()


def tokenize(expresion: str):
    token_pattern = r"\d+\.\d+|\d+|[a-zA-Z_]+|[+\-*/^(),]"
    tokens = re.findall(token_pattern, expresion)
    return tokens


#tokens = tokenize("r(3, 27)")
#print(tokens)


def shunting_yard(tokens):
    output_queue = []
    operator_stack = []

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "mod": 2,
        "^": 3,
        "**": 3,
        "sin": 4,
        "cos": 4,
        "tan": 4,
        "cot": 4,
        "log": 4,
        "sqrt": 4,
        "fac": 4,
        "choose": 4
    }

    for token in tokens:
        if token == '(':
            operator_stack.append(token)
            continue

        if token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())

            if not operator_stack:
                raise ValueError("Brakujący nawias otwierający '('")

            operator_stack.pop()

            if operator_stack:
                top = operator_stack[-1]
                if top in strategy_map:
                    strategy = strategy_map[top]
                    if isinstance(strategy, UnaryOperation):
                        output_queue.append(operator_stack.pop())
            continue
        if token == ',':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            continue
        try:
            output_queue.append(float(token))
            continue
        except ValueError:
            pass

        if token in strategy_map:
            strategy = strategy_map[token]

            while operator_stack:
                top = operator_stack[-1]
                if top in strategy_map and precedence[token] <= precedence.get(top, 0):
                    output_queue.append(operator_stack.pop())
                else:
                    break

            operator_stack.append(token)
            continue

        raise ValueError(f"Nieznany token: {token}")

    while operator_stack:
        op = operator_stack.pop()
        if op in ("(", ")"):
            raise ValueError("Niezrównoważone nawiasy")
        output_queue.append(op)

    return output_queue


expression = "sqrt(2^2 + 3^2)"
tokens = tokenize(expression)
print("Tokeny:", tokens)
rpn = shunting_yard(tokens)
print("RPN: ", rpn)
result = evaluate_rpn_with_strategies(rpn)
print("Wynik:", result)