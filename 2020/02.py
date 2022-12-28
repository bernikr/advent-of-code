import re


def part1(a):
    return len([True for min, max, letter, string in (re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a)
                if int(min) <= string.count(letter) <= int(max)])


def part2(a):
    return len([True for pos1, pos2, letter, string in (re.match(r"^(\d+)-(\d+) (\w): (.+)$", i).groups() for i in a)
                if (string[int(pos1) - 1] == letter) ^ (string[int(pos2) - 1] == letter)])


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
