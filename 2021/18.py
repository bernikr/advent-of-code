from __future__ import annotations

import math
import operator
from copy import deepcopy
from enum import Enum, auto
from functools import reduce
from itertools import permutations
from typing import Optional

from tqdm import tqdm


class Side(Enum):
    LEFT = auto()
    RIGHT = auto()

    def __neg__(self):
        if self == self.LEFT:
            return self.RIGHT
        else:
            return self.LEFT


class Num:
    child: dict[Side, int | Num]
    parent: Optional[Num] = None
    slot: Optional[Side] = None

    def __init__(self, left, right):
        self.child = {
            Side.LEFT: left,
            Side.RIGHT: right
        }
        if isinstance(self.left, Num):
            self.left.parent = self
            self.left.slot = Side.LEFT
        if isinstance(self.right, Num):
            self.right.parent = self
            self.right.slot = Side.RIGHT

    @property
    def left(self):
        return self.child[Side.LEFT]

    @property
    def right(self):
        return self.child[Side.RIGHT]

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def __add__(self, other):
        return reduce_num(Num(self, other))

    def __deepcopy__(self, memodict={}):
        return Num(deepcopy(self.left), deepcopy(self.right))


def parse(s, pos=0):
    if s[pos] == '[':
        a, pos = parse(s, pos + 1)
        b, pos = parse(s, pos)
        return Num(a, b), pos + 1
    else:
        assert s[pos].isdigit()
        npos = min(s.index(',', pos) if ',' in s[pos:] else math.inf,
                   s.index(']', pos) if ']' in s[pos:] else math.inf)
        return int(s[pos:npos]), npos + 1


def max_depth(num):
    return 1 + max((max_depth(c) for c in num.child.values() if isinstance(c, Num)), default=0)


def max_num(num):
    if isinstance(num, Num):
        return max(max_num(c) for c in num.child.values())
    else:
        return num


def find_exploding_pair(num, depth=0):
    if not isinstance(num, Num):
        return None
    if depth == 4:
        return num
    if (p := find_exploding_pair(num.left, depth + 1)) is not None:
        return p
    else:
        return find_exploding_pair(num.right, depth + 1)


def add_extreme_child(num, side, add):
    if isinstance(num.child[side], Num):
        add_extreme_child(num.child[side], side, add)
    else:
        num.child[side] += add


def add_side_of(num, side, add):
    if num.slot == side:
        add_side_of(num.parent, side, add)
    elif num.parent is not None and isinstance(num.parent.child[side], Num):
        add_extreme_child(num.parent.child[side], -side, add)
    elif num.parent is not None:
        num.parent.child[side] += add


def explode(num):
    p = find_exploding_pair(num)
    add_side_of(p, Side.LEFT, p.left)
    add_side_of(p, Side.RIGHT, p.right)
    p.parent.child[p.slot] = 0


def find_split_candidate(num):
    if isinstance(num.left, int) and num.left > 9:
        return num, Side.LEFT
    if isinstance(num.left, Num) and (res := find_split_candidate(num.left)) is not None:
        return res
    if isinstance(num.right, int) and num.right > 9:
        return num, Side.RIGHT
    if isinstance(num.right, Num) and (res := find_split_candidate(num.right)) is not None:
        return res


def split(num):
    p, s = find_split_candidate(num)
    n = p.child[s]
    p.child[s] = Num(n // 2, (n + 1) // 2)
    p.child[s].parent = p
    p.child[s].slot = s


def reduce_num(num):
    num = deepcopy(num)
    while max_depth(num) > 4 or max_num(num) > 9:
        if max_depth(num) > 4:
            explode(num)
        elif max_num(num) > 9:
            split(num)
    return num


def magnitude(num):
    if isinstance(num, Num):
        return 3 * magnitude(num.left) + 2 * magnitude(num.right)
    return num


def part1(inp):
    return magnitude(reduce(operator.add, inp))


def part2(inp):
    return max((magnitude(x + y) for x, y in tqdm(permutations(inp, 2), total=len(inp) ** 2 - len(inp))))


def solve(inp, ispart1):
    inp = [parse(l)[0] for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
