from itertools import pairwise, groupby


def part1(a):
    return len([i for i in range(*a) if
                any(a == b for a, b in pairwise(str(i))) and
                all(a <= b for a, b in pairwise(str(i)))])


def part2(a):
    return len([i for i in range(*a) if
                any(len(list(a[1])) == 2 for a in groupby(str(i))) and
                all(a <= b for a, b in pairwise(str(i)))])


def solve(inp, ispart1):
    inp = tuple(map(int, inp.split('-')))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
