from collections import defaultdict

from aocd import get_data


def execute(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    def resolve(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    ip = 0
    while ip < len(p):
        match p[ip]:
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
        ip += 1
    return regs


def part1(inp):
    return execute(inp)['a']


def part2(inp):
    return execute(inp, {'c': 1})['a']


if __name__ == '__main__':
    data = get_data(day=12, year=2016)
    inp = [tuple(l.split(' ')) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
