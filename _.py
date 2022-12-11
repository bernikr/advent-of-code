from aocd import data, submit, AocdError


def solve(inp, part1):
    inp = inp.splitlines()
    print(inp)
    if part1:
        return None  # Part1
    else:
        return None  # Part2


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
