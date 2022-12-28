import itertools


def part1(a):
    return sum(a)


def part2(a):
    seen = set()
    f = 0
    for i in itertools.cycle(a):
        if f in seen:
            return f
        seen.add(f)
        f += i


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
