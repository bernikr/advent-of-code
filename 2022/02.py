def solve1(inp):
    return sum([3, 0, 6][(a - b + 3) % 3] + b for a, b in inp)


def solve2(inp):
    return sum((a + b) % 3 + 1 + [0, 0, 3, 6][b] for a, b in inp)


def solve(inp, part1):
    inp = [tuple(map(lambda x: {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}[x], l.split(' ')))
           for l in inp.splitlines()]
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
