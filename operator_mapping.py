from strategies import (
    add, sub, mul, div, mod, root, pow, choose, fac, log,
    sin, cos, tan, cot,
    arcsin, arccos, arctan,
    sinh, cosh, tanh
)

symbol_to_strategy = {
    "+": add.AddStrategy, "a": add.AddStrategy, "A": add.AddStrategy,
    "-": sub.SubStrategy, "s": sub.SubStrategy, "S": sub.SubStrategy,
    "*": mul.MulStrategy, "m": mul.MulStrategy, "M": mul.MulStrategy,
    "/": div.DivStrategy, "d": div.DivStrategy, "D": div.DivStrategy,
    "%": mod.ModStrategy, "mod": mod.ModStrategy,
    "^": pow.PowStrategy, "p": pow.PowStrategy, "P": pow.PowStrategy,
    "r": root.RootStrategy, "R": root.RootStrategy,
    "c": choose.ChooseStrategy, "C": choose.ChooseStrategy, "choose": choose.ChooseStrategy,
    "!": fac.FactorialStrategy, "fac": fac.FactorialStrategy,
    "log": log.LogStrategy,

    "sin": sin.SinusStrategy,
    "cos": cos.CosinusStrategy,
    "tan": tan.TangensStrategy,
    "cot": cot.CotangensStrategy,

    "arcsin": arcsin.ArcSinusStrategy,
    "arccos": arccos.ArcCosinusStrategy,
    "arctan": arctan.ArcTangensStrategy,

    "sinh": sinh.SinhStrategy,
    "cosh": cosh.CoshStrategy,
    "tanh": tanh.TanhStrategy
}

strategy_to_symbol = {
    'add': 'a',
    'sub': 's',
    'mul': 'm',
    'div': 'd',
    'mod': 'mod',
    'root': 'r',
    'pow': 'p',
    'choose': 'c',
    'fac': 'fac',
    'log': 'log',
    'sin': 'sin',
    'cos': 'cos',
    'tan': 'tan',
    'cot': 'cot',
    'arcsin': 'arcsin',
    'arccos': 'arccos',
    'arctan': 'arctan',
    'sinh': 'sinh',
    'cosh': 'cosh',
    'tanh': 'tanh'
}
