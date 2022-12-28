def part1(a):
    houses = [0 for _ in range(a // 10)]
    for elf in range(1, a // 10):
        for house in range(elf, a // 10, elf):
            houses[house] += elf * 10
        if houses[elf] >= a:
            return elf


def part2(a):
    houses = [0 for _ in range(a // 10)]
    for elf in range(1, a // 10):
        for house in range(elf, min(50 * elf, a // 10), elf):
            houses[house] += elf * 11
        if houses[elf] >= a:
            return elf


def solve(inp, ispart1):
    inp = int(inp)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
