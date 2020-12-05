import re

from aocd import get_data


def part1(a):
    return len([True for min, max, letter, string in [re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a]
                if int(min) <= string.count(letter) <= int(max)])


def part2(a):
    return len([True for pos1, pos2, letter, string in [re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a]
                if (string[int(pos1) - 1] == letter) ^ (string[int(pos2) - 1] == letter)])


if __name__ == '__main__':
    data = get_data(day=2, year=2020)
    input = data.splitlines()
    print(part1(input))
    print(part2(input))
