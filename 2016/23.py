from collections import defaultdict

from aocd import get_data


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


def execute(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    def resolve(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    toggled = defaultdict(lambda: False)
    ip = 0
    while ip < len(p):
        match toggle_ins(p[ip], toggled[ip]):
            case ('cpy', x, y):
                regs[y] = resolve(x)
            case ('inc', x):
                regs[x] += 1
            case ('dec', x):
                regs[x] -= 1
            case ('jnz', x, y):
                if resolve(x) != 0:
                    ip += resolve(y)
                    continue
            case ('tgl', x):
                toggled[ip + resolve(x)] = not toggled[ip + resolve(x)]
            case x:
                raise NotImplementedError(x)
        ip += 1
    return regs


def part1(inp):
    return execute(inp, {'a': 7})['a']


def part2(inp):
    return execute(inp, {'a': 12})['a']


if __name__ == '__main__':
    data = get_data(day=23, year=2016)
    inp = [tuple(l.split(' ')) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
