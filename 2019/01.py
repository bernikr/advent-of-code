from aocd import get_data


def part1(a):
    return sum(m // 3 - 2 for m in a)


def calculate_recursive_fuel(mass):
    if mass <= 0:
        return 0
    else:
        return max(0, mass // 3 - 2) + calculate_recursive_fuel(mass // 3 - 2)


def part2(a):
    return sum(calculate_recursive_fuel(m) for m in a)


if __name__ == '__main__':
    data = get_data(day=1, year=2019)
    inp = list(map(int, data.splitlines()))
    print(part1(inp))
    print(part2(inp))
