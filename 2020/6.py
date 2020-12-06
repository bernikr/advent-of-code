from aocd import get_data


def part1(a):
    return sum([len(set(g.replace('\n', ''))) for g in a])


def part2(a):
    return sum([len(set.intersection(*[set(l) for l in g.split('\n')])) for g in a])


if __name__ == '__main__':
    data = get_data(day=6, year=2020)
    input = data.split('\n\n')
    print(part1(input))
    print(part2(input))
