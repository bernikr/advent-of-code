import operator
import re
from functools import reduce
from itertools import groupby
from operator import itemgetter


def solve(inp, part1):
    GAME_RE = re.compile(r"Game (\d+)")
    COLOR_RE = re.compile(r"(\d+) (blue|green|red)")
    inp = {int(GAME_RE.match(l).group(1)): [(b, int(a)) for a, b in COLOR_RE.findall(l)] for l in inp.splitlines()}
    if part1:
        maximums = {"red": 12, "green": 13, "blue": 14}
        return sum(k for k, v in inp.items() if all(count <= maximums[col] for col, count in v))
    else:
        return sum(reduce(operator.mul,
                          map(itemgetter(1),
                              (max(vals) for col, vals in groupby(sorted(g, key=itemgetter(0)), itemgetter(0)))))
                   for g in inp.values())


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
