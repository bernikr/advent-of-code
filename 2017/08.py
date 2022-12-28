from collections import defaultdict
from itertools import chain


def execute(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    def r(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    maxv = 0
    ip = 0
    while ip < len(p):
        ins, cond = p[ip]
        cond_res = False
        match cond:
            case (a, '>=', b):
                cond_res = r(a) >= r(b)
            case (a, '>', b):
                cond_res = r(a) > r(b)
            case (a, '<', b):
                cond_res = r(a) < r(b)
            case (a, '!=', b):
                cond_res = r(a) != r(b)
            case (a, '==', b):
                cond_res = r(a) == r(b)
            case (a, '<=', b):
                cond_res = r(a) <= r(b)
            case x:
                raise NotImplementedError(x)
        if cond_res:
            match ins:
                case (reg, 'inc', x):
                    regs[reg] += r(x)
                case (reg, 'dec', x):
                    regs[reg] -= r(x)
                case x:
                    raise NotImplementedError(x)
        maxv = max(chain([maxv], regs.values()))
        ip += 1
    return regs, maxv


def solve(inp, ispart1):
    inp = [(tuple(l.split(' ')[0:3]), tuple(l.split(' ')[4:])) for l in inp.splitlines()]
    res = execute(inp)
    return max(res[0].values()) if ispart1 else res[1]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
