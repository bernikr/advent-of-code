from functools import reduce


def part1(a):
    return sum([l[i * 3 % len(l)] for i, l in enumerate(a)])


def part2(a):
    return reduce(lambda x, y: x * y, [sum([l[i * r % len(l)] for i, l in enumerate(a[::d])])
                                       for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])


if __name__ == '__main__':
    with open("3.input") as f:
        input = [[c == '#' for c in l.strip()] for l in f.readlines()]
    print(part1(input))
    print(part2(input))
