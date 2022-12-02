from aocd import data, submit, AocdError


def part1(inp):
    return sum([3, 0, 6][(a - b + 3) % 3] + b for a, b in inp)


def part2(inp):
    return sum((a + b) % 3 + 1 + [0, 0, 3, 6][b] for a, b in inp)


if __name__ == '__main__':
    inp = [tuple(map(lambda x: {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}[x], l.split(' ')))
           for l in data.splitlines()]
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
