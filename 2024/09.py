from collections.abc import Iterable
from typing import Literal

from more_itertools import grouper


def get_length(store: list[int], pointer: int, direction: Literal[-1, 1]) -> int:
    c = store[pointer]
    i = 0
    while 0 <= pointer + direction * i < len(store) and store[pointer + direction * i] == c:
        i += 1
    return i


def part1(storage: list[int | None]) -> int:
    j = len(storage) - 1
    for i in range(len(storage)):
        if storage[i] is not None:
            continue
        while storage[j] is None:
            j -= 1
        if j <= i:
            break
        storage[i] = storage[j]
        storage[j] = None
    return sum(i * x for i, x in enumerate(storage) if x is not None)


def part2(storage: list[int | None]) -> int:
    fpointer = len(storage) - 1
    free = [0] * 10
    while fpointer >= 0:
        if storage[fpointer] is None:
            fpointer -= 1
        file_length = get_length(storage, fpointer, -1)
        while storage[free[file_length]] is not None or get_length(storage, free[file_length], 1) < file_length:
            free[file_length] += get_length(storage, free[file_length], 1)
        if free[file_length] < fpointer:
            storage[free[file_length]:free[file_length] + file_length] \
                = storage[fpointer - file_length + 1:fpointer + 1]
            storage[fpointer - file_length + 1:fpointer + 1] = [None] * file_length
        fpointer -= file_length
    return sum(i * x for i, x in enumerate(storage) if x is not None)


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp = [int(c) for c in inp]
    length = sum(inp)
    storage: list[int | None] = [None] * length
    cur = 0
    for i, (a, b) in enumerate(grouper(inp, 2, fillvalue=0)):
        for j in range(a):
            storage[cur + j] = i
        cur += a + b

    yield 1, part1(storage.copy())
    yield 2, part2(storage)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
