from collections import defaultdict
from itertools import count, cycle


def resolve(regs, x):
    try:
        return int(x)
    except ValueError:
        return regs[x]


def execute(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    ip = 0
    while ip < len(p):
        match p[ip]:
            case ('cpy', x, y):
                regs[y] = resolve(regs, x)
            case ('inc', x):
                regs[x] += 1
            case ('dec', x):
                regs[x] -= 1
            case ('jnz', x, y):
                if resolve(regs, x) != 0:
                    ip += resolve(regs, y)
                    continue
            case ('out', x):
                yield resolve(regs, x)
            case x:
                raise NotImplementedError(x)
        ip += 1


def part1(inp):
    for i in count():
        for n, (r, o) in enumerate(zip(cycle([0, 1]), execute(inp, {'a': i}))):
            if r != o:
                break
            if n > 100:
                return i


def solve(inp, ispart1):
    inp = [tuple(l.split(' ')) for l in inp.splitlines()]
    return part1(inp) if ispart1 else None


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
    except AocdError as e:
        print(e)
