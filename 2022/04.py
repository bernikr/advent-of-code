from aocd import data, submit, AocdError


def part1(inp):
    return sum(all(i in range(a, b + 1) for i in range(c, d + 1)) or all(i in range(c, d + 1) for i in range(a, b + 1))
               for (a, b), (c, d) in inp)


def part2(inp):
    return sum(any(i in range(a, b + 1) for i in range(c, d + 1)) or any(i in range(c, d + 1) for i in range(a, b + 1))
               for (a, b), (c, d) in inp)


if __name__ == '__main__':
    inp = [tuple(map(lambda x: tuple(map(int, x.split('-'))), l.split(','))) for l in data.splitlines()]
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
