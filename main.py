from Calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    while calc.keep_going:
        calc.get_input()
        print(calc.perform_operation())
