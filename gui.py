from tkinter import *
from Calculator import Calculator
from controller import CalculatorController


calc = Calculator()
history = []
controller = CalculatorController(calc, history)


def on_click():
    text = entry.get()
    result = controller.parse(text)
    label.config(text=result)


def show_history():
    hist_label.config(text="\n".join(history))


def clear_hist():
    history.clear()
    hist_label.config(text="Historia jest pusta")


root = Tk()
frame = Frame(root)
frame.pack()

entry = Entry(frame, width=20)
entry.pack()

count = Button(frame, text="Oblicz: ", command=on_click)
count.pack()

history_button = Button(frame, text="Pokaż historię", command=show_history)
history_button.pack()

clear_hist_button = Button(frame, text="Wyczyść historię", command=clear_hist)
clear_hist_button.pack()

label = Label(root, text="")
label.pack()

hist_label = Label(root, text="Historia: \n")
hist_label.pack()

root.mainloop()
