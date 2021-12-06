from collections import defaultdict

from aocd import get_data


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


def part2(inp):
    pass


if __name__ == '__main__':
    data = get_data(day=23, year=2017)
    inp = [tuple(l.split(' ')) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
