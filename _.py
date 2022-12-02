from aocd import data, submit, AocdError


def part1(inp):
    print(inp)
    return None


def part2(inp):
    return None


if __name__ == '__main__':
    inp = data.splitlines()
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
