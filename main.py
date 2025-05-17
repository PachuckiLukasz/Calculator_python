from Calculator import Calculator
import os
import platform


def clear_screen():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    except:
        print("\n" * 50)


if __name__ == "__main__":
    calc = Calculator()
    while calc.keep_going:
        print("-" * 30)
        calc.get_input()
        print(calc.perform_operation())
        input("\nNaciśnij Enter, aby kontynuować...")
        clear_screen()
        print("-" * 30)
        print()
