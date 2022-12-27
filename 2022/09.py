from itertools import chain

from aoc_utils import Vec, sign


def move_rope(inp, rope_length):
    rope = [Vec(0, 0) for _ in range(rope_length)]
    tail_pos = {rope[-1]}
    for ins in chain.from_iterable((d for _ in range(i)) for d, i in inp):
        rope[0] += {"U": Vec(0, 1), "D": Vec(0, -1), "L": Vec(-1, 0), "R": Vec(1, 0)}[ins]
        for i in range(1, rope_length):
            if abs(rope[i - 1] - rope[i]) >= 2:
                rope[i] += Vec(*map(sign, rope[i - 1] - rope[i]))
        tail_pos.add(rope[-1])
    return len(tail_pos)


def solve(inp, part1):
    inp = [(l[0], int(l[2:])) for l in inp.splitlines()]
    return move_rope(inp, 2 if part1 else 10)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
