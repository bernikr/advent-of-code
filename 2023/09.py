from itertools import pairwise


def predict_next(history):
    if not any(history):
        return 0
    return history[-1] + predict_next([b - a for a, b in pairwise(history)])


def solve(inp, part1):
    return sum(predict_next(x[::1 if part1 else -1]) for x in (list(map(int, l.split())) for l in inp.splitlines()))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
