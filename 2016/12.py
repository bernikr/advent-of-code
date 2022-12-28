from collections import defaultdict


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


def solve(inp, part1):
    inp = [tuple(l.split(' ')) for l in inp.splitlines()]
    return execute(inp, {} if part1 else {'c': 1})['a']


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
