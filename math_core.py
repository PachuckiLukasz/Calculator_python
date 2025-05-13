from strategies import AddStrategy, SubStrategy, MulStrategy, PowStrategy, DivStrategy, ModStrategy,RootStrategy, LogStrategy

operations = {
    "A": AddStrategy(),
    "S": SubStrategy(),
    "M": MulStrategy(),
    "P": PowStrategy(),
    "D": DivStrategy(),
    "MOD": ModStrategy(),
    "R": RootStrategy(),
}
single_arg_operations ={
    "LOG": LogStrategy(),
}


def compute(first_num, second_num, operator):
    if operator in operations:
        return operations[operator].execute(first_num, second_num)
    raise ValueError("Błąd: Nieznana operacja")


def compute_single_argument(first_num, operator):
    import math
    if operator == "LOG":
        if first_num > 0:
            return math.log10(first_num)
        raise ValueError("Błąd: liczba musi być większa od zera")
