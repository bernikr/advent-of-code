from itertools import product

from aocd import get_data


def part1(a):
    a = [int(i.strip()) for i in a]
    a = product(a, a)
    for i in a:
        if i[0]+i[1] == 2020:
            return i[0]*i[1]


def part2(a):
    a = [int(i.strip()) for i in a]
    a = product(a, repeat=3)
    for i in a:
        if i[0]+i[1]+i[2] == 2020:
            return i[0]*i[1]*i[2]


if __name__ == '__main__':
    data = get_data(day=1, year=2020)
    input = data.splitlines()
    print(part1(input))
    print(part2(input))
