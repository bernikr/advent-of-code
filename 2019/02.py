import itertools

from aocd import get_data


def execute(p):
    p = p.copy()
    ip = 0
    while True:
        if p[ip] == 1:
            p[p[ip + 3]] = p[p[ip + 1]] + p[p[ip + 2]]
        elif p[ip] == 2:
            p[p[ip + 3]] = p[p[ip + 1]] * p[p[ip + 2]]
        elif p[ip] == 99:
            return p
        ip += 4


def part1(a):
    p = a.copy()
    p[1] = 12
    p[2] = 2
    return execute(p)[0]


def part2(a):
    for n, v in itertools.product(range(100), repeat=2):
        p = a.copy()
        p[1] = n
        p[2] = v
        if execute(p)[0] == 19690720:
            return 100 * n + v


if __name__ == '__main__':
    data = get_data(day=2, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
