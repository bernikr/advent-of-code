import math
import operator
import re
from collections import Counter
from collections.abc import Iterable
from functools import reduce
from itertools import count
from statistics import variance
from typing import Any

from more_itertools import grouper
from tqdm import tqdm

from aoc_utils import Vec, sign
from aocd_runner import NO_EXTRA, aocd_run_solver


def solve(inp: str, extra: dict[str, Any] = NO_EXTRA) -> Iterable[tuple[int, int | str]]:
    if extra is None:
        extra = {}
    inp = [
        tuple(Vec(p) for p in grouper(map(int, x), 2)) for x in re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", inp)
    ]
    floor_size = Vec(extra.get("width", 101), extra.get("height", 103))
    middle = (floor_size - Vec(1, 1)) / 2
    yield (
        1,
        reduce(
            operator.mul,
            (
                c
                for d, c in Counter(
                    tuple(map(sign, (p + 100 * v).pos_mod(floor_size) - middle)) for p, v in inp
                ).items()
                if all(x != 0 for x in d)
            ),
        ),
    )

    # assumes that the tree is the configuration with the smallest variance
    variance_record = math.inf
    record_id = 0
    for i in tqdm(count()):
        if i > record_id + 8000:  # assumes that if no lower variance is found after 5000 iterations, we have found it
            break
        poss = [(p + i * v).pos_mod(floor_size) for p, v in inp]
        a = variance(map(operator.itemgetter(0), poss)) * variance(map(operator.itemgetter(1), poss))
        if a < variance_record:
            variance_record = a
            record_id = i
    yield 2, record_id


if __name__ == "__main__":
    aocd_run_solver(solve)
