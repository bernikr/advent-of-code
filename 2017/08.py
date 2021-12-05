from collections import defaultdict
from itertools import chain

from aocd import get_data


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


def part1(inp):
    return max(execute(inp)[0].values())


def part2(inp):
    return execute(inp)[1]


if __name__ == '__main__':
    data = get_data(day=8, year=2017)
    inp = [(tuple(l.split(' ')[0:3]), tuple(l.split(' ')[4:])) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
