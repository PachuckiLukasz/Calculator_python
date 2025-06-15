from rpn_strategy_map import strategy_map

operations = {
    "a": strategy_map["+"],
    "s": strategy_map["-"],
    "m": strategy_map["*"],
    "p": strategy_map["^"],
    "d": strategy_map["/"],
    "mod": strategy_map["%"],
    "r": strategy_map["r"],
    "c": strategy_map["choose"],
}

single_arg_operations = {
    "log": strategy_map["log"],
    "fac": strategy_map["fac"],
    "sin": strategy_map["sin"],
    "cos": strategy_map["cos"],
    "tan": strategy_map["tan"],
    "cot": strategy_map["cot"],
    "arcsin": strategy_map["arcsin"],
    "arccos": strategy_map["arccos"],
    "arctan": strategy_map["arctan"],
    "sinh": strategy_map["sinh"],
    "cosh": strategy_map["cosh"],
    "tanh": strategy_map["tanh"],
}


def compute(first_num, second_num, operator):
    operator = operator.lower()
    if operator in operations:
        return operations[operator].execute(first_num, second_num)
    raise ValueError("Błąd: Nieznana operacja")


def compute_unary(first_num, operator):
    operator = operator.lower()
    if operator in single_arg_operations:
        return single_arg_operations[operator].execute(first_num)
    raise ValueError("Nieznana operacja jednoargumentowa")
