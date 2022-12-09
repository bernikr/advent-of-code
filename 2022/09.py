from itertools import chain

from aoc_utils import Vec, sign
from aocd import data, submit, AocdError

dirs = {"U": Vec(0, 1), "D": Vec(0, -1), "L": Vec(-1, 0), "R": Vec(1, 0)}


def part1(inp):
    head = Vec(0, 0)
    tail = head
    tail_pos = {tail}
    for ins in chain.from_iterable((d for _ in range(i)) for d, i in inp):
        head += dirs[ins]
        if abs(head - tail) >= 2:
            tail += Vec(*map(sign, head - tail))
            tail_pos.add(tail)
    return len(tail_pos)


def part2(inp):
    rope = [Vec(0, 0) for _ in range(10)]
    tail_pos = {rope[-1]}
    for ins in chain.from_iterable((d for _ in range(i)) for d, i in inp):
        rope[0] += dirs[ins]
        for i in range(1, 10):
            if abs(rope[i - 1] - rope[i]) >= 2:
                rope[i] += Vec(*map(sign, rope[i - 1] - rope[i]))
        tail_pos.add(rope[-1])
    return len(tail_pos)


if __name__ == '__main__':
    inp = [(l[0], int(l[2:])) for l in data.splitlines()]
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
