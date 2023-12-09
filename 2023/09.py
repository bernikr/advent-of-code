from itertools import pairwise


def predict_next(history):
    if all(x == 0 for x in history):
        return 0
    return history[-1] + predict_next([b - a for a, b in pairwise(history)])


def solve(inp, part1):
    inp = [list(map(int, l.split())) for l in inp.splitlines()]
    dir = 1 if part1 else -1
    return sum(predict_next(x[::dir]) for x in inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
