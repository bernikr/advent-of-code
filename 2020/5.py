from aocd import get_data


def part1(a):
    return max(a)


def part2(a):
    return next(i for i in range(min(a), max(a)) if i not in a and i + 1 in a and i - 1 in a)


if __name__ == '__main__':
    data = get_data(day=5, year=2020)
    inp = [int(''.join({"F": "0", "B": "1", "L": "0", "R": "1"}[c] for c in l.strip()), 2) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
