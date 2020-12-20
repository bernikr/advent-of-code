from aocd import get_data


def part1(a):
    return sum(len(l) - len(l.encode('utf-8').decode('unicode_escape')) + 2 for l in a)


def part2(a):
    return sum(len(l.encode('unicode_escape').decode('utf-8').replace('"', '\\"')) - len(l) + 2 for l in a)


if __name__ == '__main__':
    data = get_data(day=8, year=2015)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
