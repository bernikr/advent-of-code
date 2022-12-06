from aocd import data, submit, AocdError


def part1(inp):
    for i in range(4, len(inp)):
        if len(set(inp[i-4:i])) == 4:
            return i


def part2(inp):
    for i in range(14, len(inp)):
        if len(set(inp[i-14:i])) == 14:
            return i


if __name__ == '__main__':
    inp = data.strip()
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
