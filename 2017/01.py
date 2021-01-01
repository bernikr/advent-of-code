from aocd import get_data


def part1(a):
    return sum(n for i, n in enumerate(a) if n == a[(i + 1) % len(a)])


def part2(a):
    return sum(n for i, n in enumerate(a) if n == a[(i + len(a) // 2) % len(a)])


if __name__ == '__main__':
    data = get_data(day=1, year=2017)
    inp = list(map(int, data))
    print(part1(inp))
    print(part2(inp))
