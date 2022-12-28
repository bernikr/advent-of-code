from itertools import accumulate


def solve(inp, part1):
    if part1:
        return sum(map(lambda x: 1 if x == '(' else -1, inp))
    else:
        return next(i + 1 for i, n in enumerate(accumulate(map(lambda x: 1 if x == '(' else -1, inp))) if n < 0)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
