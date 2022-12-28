from collections import defaultdict


def run(a, limit):
    d = defaultdict(list)
    lastnum = 0
    for i in range(1, limit + 1):
        if i <= len(a):
            lastnum = a[i - 1]
        else:
            lastnum = 0 if len(d[lastnum]) < 2 else i - 1 - d[lastnum][-2]
        d[lastnum].append(i)
    return lastnum


def part1(a):
    return run(a, 2020)


def part2(a):
    return run(a, 30000000)


def solve(inp, ispart1):
    inp = [int(i) for i in inp.split(',')]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
