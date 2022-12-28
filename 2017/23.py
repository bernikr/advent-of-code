from collections import defaultdict

from sympy import isprime


def execute(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    def r(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    ip = 0
    ins_count = defaultdict(lambda: 0)
    while ip < len(p):
        ins_count[p[ip][0]] += 1
        match p[ip]:
            case ('set', x, y):
                regs[x] = r(y)
            case ('sub', x, y):
                regs[x] -= r(y)
            case ('mul', x, y):
                regs[x] *= r(y)
            case ('jnz', x, y):
                if r(x) != 0:
                    ip += r(y)
                    continue
            case x:
                raise NotImplementedError(x)
        ip += 1
    return regs, ins_count


def part1(inp):
    return execute(inp)[1]['mul']


# see 23.txt for steps
def manually_decompiled_code(a=0):
    b = 99
    c = b

    if a != 0:
        b *= 100
        b += 100000
        c = b
        c += 17000

    return sum(not isprime(n) for n in range(b, c + 1, 17))


def part2(inp):
    return manually_decompiled_code(1)


def solve(inp, ispart1):
    inp = [tuple(l.split(' ')) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
