from itertools import chain, combinations


def solve(inp, part1):
    inp = list(map(int, inp.splitlines()))
    if part1:
        return sum(sum(c) == 150 for c in chain.from_iterable(combinations(inp, i) for i in range(len(inp))))
    else:
        lengths = [len(c) for c in chain.from_iterable(combinations(inp, i) for i in range(len(inp))) if sum(c) == 150]
        return len([l for l in lengths if l == min(lengths)])


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
