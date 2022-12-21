import re

from aocd import data, submit, AocdError
from frozendict import frozendict
import sympy as sp

exp = re.compile(r"[a-z]{4}")


def evaluate(var, formulas, humn=None):
    if var == "humn" and humn is not None:
        return humn
    return eval(formulas[var], {v: evaluate(v, formulas, humn) for v in exp.findall(formulas[var])})


def solve(inp, part1):
    inp = {l[:4]: l[6:] for l in inp.splitlines()}
    if part1:
        return int(evaluate('root', frozendict(inp)))
    else:
        humn = sp.symbols('humn')
        a, b = map(lambda x: evaluate(x, frozendict(inp), humn), exp.findall(inp['root']))
        return int(sp.solve(sp.Eq(a, b), humn)[0])


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
