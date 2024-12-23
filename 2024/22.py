from collections import Counter
from collections.abc import Iterable
from itertools import accumulate, pairwise

from more_itertools import windowed
from tqdm import tqdm


def step(x: int) -> int:
    x ^= x << 6
    x &= (1 << 24) - 1
    x ^= x >> 5
    x ^= x << 11
    x &= (1 << 24) - 1
    return x


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [int(x) for x in inp.splitlines()]
    sequences = [list(accumulate(range(2000), lambda x, _: step(x), initial=i)) for i in tqdm(inp)]
    yield 1, sum(s[-1] for s in sequences)

    c = Counter()
    for s in tqdm(sequences):
        prices = [x % 10 for x in s]
        diffs = [b - a for a, b in pairwise(prices)]
        found = set()
        for w, p in zip(windowed(diffs, 4), prices[4:], strict=True):
            if w not in found:
                found.add(w)
                c[w] += p
    yield 2, max(c.values())


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
