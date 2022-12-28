def part1(a):
    return sum(len(set(g.replace('\n', ''))) for g in a)


def part2(a):
    return sum(len(set.intersection(*[set(l) for l in g.split('\n')])) for g in a)


def solve(inp, ispart1):
    inp = inp.split('\n\n')
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
