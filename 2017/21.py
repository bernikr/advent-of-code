from collections import Counter, defaultdict

from aoc_utils import Vec


def parse_pattern(p):
    lines = p.split('/')
    s = len(lines)
    return s, frozenset(
        {Vec(x - (s - 1) / 2, y - (s - 1) / 2) for y, l in enumerate(lines) for x, c in enumerate(l) if c == '#'})


def rotate_and_flip(pattern):
    s, p = pattern
    yield from rotate(pattern)
    yield from rotate((s, {Vec(-x, y) for x, y in p}))


def rotate(pattern):
    s, p = pattern
    yield s, p
    yield s, {Vec(-y, x) for x, y in p}
    yield s, {Vec(-x, -y) for x, y in p}
    yield s, {Vec(y, -x) for x, y in p}


def sector_coord_range(grid_size, sector_size):
    assert grid_size % sector_size == 0
    steps = grid_size // sector_size
    for i in range(steps):
        yield -grid_size / 2 + sector_size / 2 + sector_size * i


def split_into_tiles(grid):
    grid_s, grid_p = grid
    if grid_s % 2 == 0:
        sector_size = 2
    else:
        assert grid_s % 3 == 0
        sector_size = 3
    tiles = {}
    for sx in sector_coord_range(grid_s, sector_size):
        for sy in sector_coord_range(grid_s, sector_size):
            tile_pos = Vec(sx, sy)
            sector = frozenset(filter(lambda p: all(abs(c) <= (sector_size - 1) / 2 for c in p),
                                      {p - tile_pos for p in grid_p}))
            tiles[tile_pos] = (sector_size, sector)
    return tiles


def step(grid, rules):
    grid_s, grid_p = grid
    new_grid = set()
    if grid_s % 2 == 0:
        sector_size = 2
        new_sector_size = 3
    else:
        assert grid_s % 3 == 0
        sector_size = 3
        new_sector_size = 4
    for tile_pos, (_, sector) in split_into_tiles(grid).items():
        s, new_sector = rules[sector_size, sector]
        assert s == new_sector_size
        new_grid |= {p + tile_pos / sector_size * new_sector_size for p in new_sector}
    return grid_s // sector_size * new_sector_size, frozenset(new_grid)


def solve(inp, part1):
    inp = [l.split(' => ') for l in inp.splitlines()]
    pattern_to_id = {}
    pattern_fill = {}
    pattern_rules = {}
    for i, (pattern, result) in enumerate(inp):
        pattern_fill[i] = sum(1 if c == '#' else 0 for c in pattern)
        for s, p in rotate_and_flip(parse_pattern(pattern)):
            pattern_to_id[s, frozenset(p)] = i
            pattern_rules[s, frozenset(p)] = parse_pattern(result)

    # every third iteration is not divisible by 3
    # so we can step every tile 3 times and record the ids and count of the resulting tiles
    tripplestep_map = {}
    for pattern, _ in inp:
        p = parse_pattern(pattern)
        i = pattern_to_id[p]
        for _ in range(3):
            p = step(p, pattern_rules)
        tripplestep_map[i] = dict(Counter([pattern_to_id[t] for t in split_into_tiles(p).values()]))

    # load the initial grid and step it manually until the remaining steps are a multiple of 3
    grid = parse_pattern('.#./..#/###')
    iterations = 5 if part1 else 18
    while iterations % 3 != 0:
        grid = step(grid, pattern_rules)
        iterations -= 1

    # do the remaining iterations 3 at a time while only keeping track of the used tiles
    grid_counter = dict(Counter([pattern_to_id[t] for t in split_into_tiles(grid).values()]))
    for _ in range(iterations // 3):
        new_grid_counter = defaultdict(int)
        for p, c in grid_counter.items():
            for res_p, res_c in tripplestep_map[p].items():
                new_grid_counter[res_p] += c * res_c
        grid_counter = new_grid_counter
    return sum(pattern_fill[p] * c for p, c in grid_counter.items())


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
