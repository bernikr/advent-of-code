from aocd import data, submit, AocdError


def part1(inp):
    return max(map(sum, inp))


def part2(inp):
    return sum(sorted(map(sum, inp))[-3:])


if __name__ == '__main__':
    inp = [[int(x) for x in l.splitlines()] for l in data.split('\n\n')]
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
