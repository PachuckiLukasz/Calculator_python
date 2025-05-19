from tkinter import *

from Calculator import Calculator

calc = Calculator()


def parse_input(text: str):
    operators = ['+', '-', '*', '/', '%', '^']
    symbol_to_strategy = {
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
        '%': 'mod',
        '^': 'pow'
    }
    strategy_to_symbol = {
        'add': 'A',
        'sub': 'S',
        'mul': 'M',
        'div': 'D',
        'mod': 'MOD',
        'pow': 'P'
    }
    for operator in operators:
        try:
            if operator in text:
                print("znaleziony operator: ", operator)
                a_str, b_str = text.split(operator)
                print("Lewa liczba:", a_str, "\nPrawa liczba:", b_str)
                a = float(a_str)
                b = float(b_str)
                print("A float:", a, "\nB float:", b)
                operation_name = symbol_to_strategy[operator]
                calc.operator = strategy_to_symbol[operation_name]
                calc.first_num = a
                calc.second_num = b
                result = calc.perform_operation()
                label.config(text=f"Wynik: {result}")
                print("Wynik:", result)
        except Exception:
                label.config(text= "Błąd - nieprawidłowe dane")

def on_click():
    text = entry.get()
    parse_input(text)


root = Tk()
frame = Frame(root)
frame.pack()

entry = Entry(frame, width=20)
entry.pack()

count = Button(frame, text="Oblicz: ", command=on_click)
count.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
