import re


def part1(a):
    return len([True for min, max, letter, string in [re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a]
                if int(min) <= string.count(letter) <= int(max)])


def part2(a):
    return len([True for pos1, pos2, letter, string in [re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a]
                if (string[int(pos1) - 1] == letter) ^ (string[int(pos2) - 1] == letter)])


if __name__ == '__main__':
    with open("2.input") as f:
        input = f.readlines()
    print(part1(input))
    print(part2(input))
