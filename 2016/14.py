from functools import cache
from hashlib import md5

from aoc_utils import nth

hexdigits = '0123456789abcdef'


@cache
def calc_hash(i, salt, stretched=False):
    if not stretched:
        return md5(f"{salt}{i}".encode()).hexdigest()
    else:
        s = f"{salt}{i}"
        for _ in range(2017):
            s = md5(s.encode()).hexdigest()
        return s


def find_first_3_sequence(s):
    try:
        return next(s[i] for i in range(len(s) - 2) if s[i] == s[i + 1] == s[i + 2])
    except StopIteration:
        return None


def is_valid_hash(i, salt, stretched=False):
    h = calc_hash(i, salt, stretched)
    s = find_first_3_sequence(h)
    if not s:
        return False
    return any(s * 5 in calc_hash(j, salt, stretched) for j in range(i + 1, i + 1001))


def solve(inp, part1):
    return nth((i for i in range(22729) if is_valid_hash(i, inp, not part1)), 63)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
