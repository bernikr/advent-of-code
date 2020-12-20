from aocd import get_data


def part1(a):
    return sum(2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l) for l, w, h in a)


def part2(a):
    return sum(2 * a + 2 * b + a * b * c for a, b, c in (sorted(s) for s in a))


if __name__ == '__main__':
    data = get_data(day=2, year=2015)
    inp = [tuple(map(int, l.split('x'))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
