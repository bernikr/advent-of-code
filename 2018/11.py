import math

import numpy as np
from aoc_utils import Box
from scipy.signal import convolve2d
from tqdm import tqdm


def power(c, serial):
    if c not in Box((1, 1), (300, 300)):
        raise ValueError
    x, y = c
    rackid = x + 10
    return (((rackid * y + serial) * rackid) // 100) % 10 - 5


def max_square(grid, size):
    con = convolve2d(grid, np.ones(shape=(size, size)), "valid")
    y, x = np.unravel_index(con.argmax(), con.shape)
    return x+1, y+1, con[y, x]


def solve(inp, part1):
    serial = int(inp)
    grid = np.array([[power((x, y), serial) for x in range(1, 300)] for y in range(1, 300)])
    if part1:
        x, y, res = max_square(grid, 3)
        return f"{x},{y}"
    else:
        maxv = -math.inf
        maxargs = None
        for i in tqdm(range(1, 301)):
            x, y, res = max_square(grid, i)
            if res > maxv:
                maxv = res
                maxargs = (x, y, i)
            if res < 0:  # heuristic optimization: expected value of a cell is negative, therefore we expect large squares to be negative
                break
        return "{},{},{}".format(*maxargs)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
