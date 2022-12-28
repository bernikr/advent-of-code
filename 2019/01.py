def part1(a):
    return sum(m // 3 - 2 for m in a)


def calculate_recursive_fuel(mass):
    if mass <= 0:
        return 0
    else:
        return max(0, mass // 3 - 2) + calculate_recursive_fuel(mass // 3 - 2)


def part2(a):
    return sum(calculate_recursive_fuel(m) for m in a)


def solve(inp, ispart1):
    inp = list(map(int, inp.splitlines()))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
