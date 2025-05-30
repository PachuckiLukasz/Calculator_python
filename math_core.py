from strategies import AddStrategy, SubStrategy, MulStrategy, PowStrategy, DivStrategy, ModStrategy, \
    RootStrategy, LogStrategy, ChooseStrategy


operations = {
    "A": AddStrategy(),
    "S": SubStrategy(),
    "M": MulStrategy(),
    "P": PowStrategy(),
    "D": DivStrategy(),
    "MOD": ModStrategy(),
    "R": RootStrategy(),
    "C": ChooseStrategy(),
}
single_arg_operations = {
    "LOG": LogStrategy(),
}


def compute(first_num, second_num, operator):
    if operator in operations:
        return operations[operator].execute(first_num, second_num)
    raise ValueError("Błąd: Nieznana operacja")


def compute_unary(first_num, operator):
    if operator in single_arg_operations:
        return single_arg_operations[operator].execute(first_num)
    else:
        raise ValueError("Nieznana operacja jednoargumentowa")

