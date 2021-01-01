from aocd import get_data


def simulate(a, part2=False):
    p = a.copy()
    ip = 0
    i = 0
    while True:
        if not 0 <= ip < len(p):
            return i
        prev_ip = ip
        ip = ip + p[ip]
        p[prev_ip] += 1 if not part2 or p[prev_ip] < 3 else -1
        i += 1


def part1(a):
    return simulate(a)


def part2(a):
    return simulate(a, True)


if __name__ == '__main__':
    data = get_data(day=5, year=2017)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
