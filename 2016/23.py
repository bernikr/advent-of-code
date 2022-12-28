from collections import defaultdict


def resolve(regs, x):
    try:
        return int(x)
    except ValueError:
        return regs[x]


def toggle_ins(ins, toggled):
    if not toggled:
        return ins
    match ins:
        case ('inc', x):
            return 'dec', x
        case (_, x):
            return 'inc', x
        case ('jnz', x, y):
            return 'cpy', x, y
        case (_, x, y):
            return 'jnz', x, y


def optimize(p, regs):
    match p:
        case [('cpy', b, c), ('inc', a), ('dec', c1), ('jnz', c2, '-2'), ('dec', d), ('jnz', d1, '-5'), *_] \
          if c == c1 == c2 and d == d1:  # multiplication
            regs[a] += resolve(regs, b) * resolve(regs, d)
            regs[c] = 0
            regs[d] = 0
            return 6
        case [('inc', a), ('dec', b), ('jnz', b1, '-2'), *_] if b == b1:  # addition
            regs[a] += resolve(regs, b)
            regs[b] = 0
            return 3


def execute(p, regs={}, opt=False):
    regs = defaultdict(lambda: 0, regs)

    toggled = defaultdict(lambda: False)
    ip = 0
    while ip < len(p):
        if skip := optimize([toggle_ins(ins, toggled[i]) for i, ins in enumerate(p)][ip:], regs):
            ip += skip
            continue
        match toggle_ins(p[ip], toggled[ip]):
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
            case ('tgl', x):
                toggled[ip + resolve(regs, x)] = not toggled[ip + resolve(regs, x)]
            case x:
                raise NotImplementedError(x)
        ip += 1
    return regs


def part1(inp):
    return execute(inp, {'a': 7})['a']


def part2(inp):
    return execute(inp, {'a': 12})['a']


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
