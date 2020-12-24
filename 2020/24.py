import itertools
import operator
from collections import defaultdict
from functools import reduce

from aocd import get_data


# use axial coordinates: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
neighbors = {'e': (1, 0), 'w': (-1, 0), 'nw': (0, -1), 'ne': (1, -1), 'sw': (-1, 1), 'se': (0, 1)}


def resolve_steps(s):
    return reduce(lambda x, y: tuple(map(operator.add, x, y)), map(neighbors.get, s))


def initial_black_tiles(instructions):
    tiles = defaultdict(lambda: False)
    for s in instructions:
        t = resolve_steps(s)
        tiles[t] = not tiles[t]
    return set(k for k, v in tiles.items() if v)


def part1(a):
    return len(initial_black_tiles(a))


def get_neighbors(c):
    return list(map(lambda x: tuple(map(operator.add, c, x)), neighbors.values()))


def count_neighbors(c, tiles):
    return sum(map(lambda x: x in tiles, get_neighbors(c)))


def part2(a):
    black_tiles = initial_black_tiles(a)
    for _ in range(100):
        new_black_tiles = set()
        relevant_tiles = set(itertools.chain.from_iterable(map(get_neighbors, black_tiles)))
        for t in relevant_tiles:
            if t in black_tiles and 1 <= count_neighbors(t, black_tiles) <= 2:
                new_black_tiles.add(t)
            elif t not in black_tiles and count_neighbors(t, black_tiles) == 2:
                new_black_tiles.add(t)
        black_tiles = new_black_tiles
    return len(black_tiles)


if __name__ == '__main__':
    data = get_data(day=24, year=2020)
    inp = [l.replace('e', 'e ').replace('w', 'w ').split(' ')[:-1] for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
