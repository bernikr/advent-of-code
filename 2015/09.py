import itertools
import re


def solve(inp, part1):
    inp = [re.match(r"^(\w+) to (\w+) = (\d+)$", l).groups() for l in inp.splitlines()]
    inp = (set(itertools.chain.from_iterable((a, b) for a, b, _ in inp)),
           dict(itertools.chain.from_iterable((((a, b), int(c)), ((b, a), int(c))) for a, b, c in inp)))
    op = min if part1 else max
    return op(sum(inp[1][(r[i], r[i + 1])] for i in range(len(r) - 1)) for r in itertools.permutations(inp[0]))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
