from functools import reduce
from itertools import chain, repeat, cycle

from tqdm import tqdm

base_pattern = [0, 1, 0, -1]


def get_pattern(index):
    return list(chain.from_iterable(repeat(e, index + 1) for e in base_pattern))[1:] + [base_pattern[0]]


def apply_pattern(inp, pattern):
    return abs(sum(a * b for a, b in zip(inp, cycle(pattern)))) % 10


def phase(inp):
    return [apply_pattern(inp, get_pattern(i)) for i in range(len(inp))]


def part1(inp):
    return ''.join(map(str, reduce(lambda x, _: phase(x), range(100), inp)[:8]))


def part2(inp):
    start = int(''.join(map(str, inp[:7])))
    a = inp * 10000
    assert start >= len(a) / 2, "This method only works for special cases"
    a = a[start:]
    for _ in tqdm(range(100)):
        out = []
        s = sum(a)
        for n in a:
            out.append(s % 10)
            s -= n
        a = out
    return ''.join(map(str, a[:8]))


def solve(inp, ispart1):
    inp = list(map(int, inp))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
