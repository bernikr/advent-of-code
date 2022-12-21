import re
from functools import lru_cache

from aocd import data, submit, AocdError
from cpmpy import Model, intvar
from frozendict import frozendict

exp = re.compile(r"[a-z]{4}")


def evaluate(var, formulas, humn=None):
    if var == "humn" and humn is not None:
        return humn
    vars = {v: evaluate(v, formulas, humn) for v in exp.findall(formulas[var])}
    f = formulas[var]
    if all(isinstance(v, int) for v in vars.values()):
        f = f.replace('/', '//')
    return eval(f, vars)


def solve(inp, part1):
    inp = {l[:4]: l[6:] for l in inp.splitlines()}
    if part1:
        return evaluate('root', frozendict(inp))
    else:
        humn = intvar(0, 10 ** 15)
        a, b = map(lambda x: evaluate(x, frozendict(inp), humn), exp.findall(inp['root']))
        m = Model(a == b)
        m.solve()
        return humn.value()


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
