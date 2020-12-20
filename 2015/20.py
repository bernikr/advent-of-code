from aocd import get_data


def part1(a):
    houses = [0 for _ in range(a//10)]
    for elf in range(1, a//10):
        for house in range(elf, a//10, elf):
            houses[house] += elf*10
        if houses[elf] >= a:
            return elf


def part2(a):
    houses = [0 for _ in range(a//10)]
    for elf in range(1, a//10):
        for house in range(elf, min(50*elf, a//10), elf):
            houses[house] += elf*11
        if houses[elf] >= a:
            return elf


if __name__ == '__main__':
    data = get_data(day=20, year=2015)
    inp = int(data)
    print(part1(inp))
    print(part2(inp))
