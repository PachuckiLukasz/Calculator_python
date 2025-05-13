from strategies import AddStrategy, SubStrategy, MulStrategy, PowStrategy

operations = {
    "A": AddStrategy(),
    "S": SubStrategy(),
    "M": MulStrategy(),
    "P": PowStrategy(),

}


def compute(first_num, second_num, operator):
    if operator in operations:
        return operations[operator].execute(first_num, second_num)

# def compute(first_num, second_num, operator):
#     match operator:
#         case "A":
#             return first_num + second_num
#         case "S":
#             return first_num - second_num
#         case "M":
#             return first_num * second_num
#         case "P":
#             return first_num ** second_num
#         case "D":
#             if second_num == 0:
#                 raise ZeroDivisionError("Błąd: Nie możesz dzielić przez 0")
#             return first_num / second_num
#         case "MOD":
#             if second_num == 0:
#                 raise ZeroDivisionError("Błąd: Nie możesz dzielić przez 0")
#             return first_num % second_num
#         case "R":
#             if second_num == 0:
#                 raise ZeroDivisionError("Błąd: Nie możesz dzielić przez 0")
#             if float(second_num).is_integer() and (first_num < 0 and int(second_num % 2) == 0):
#                 raise Exception("Błąd: Wynik jest liczbą zespoloną")
#             return first_num ** (1 / second_num)
#         case _:
#             raise ValueError("Błąd: Nieznana operacja")


def compute_single_argument(first_num, operator):
    import math
    if operator == "LOG":
        if first_num > 0:
            return math.log10(first_num)
        raise ValueError("Błąd: liczba musi być większa od zera")
