import operator
import re
from functools import reduce

from aocd import get_data


def rotate_once(data):
    return [''.join(r) for r in zip(*data[::-1])]


def rotate(data, rotation):
    if rotation >= 4:
        data = [r[::-1] for r in data]
        rotation -= 4
    while rotation > 0:
        rotation -= 1
        data = rotate_once(data)
    return data


class Tile:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __repr__(self):
        return "<Tile: {}>".format(self.id)

    @staticmethod
    def parse_input(s):
        s = s.splitlines()
        id = int(re.findall(r"\d+", s[0])[0])
        data = s[1:]
        return Tile(id, data)

    def get_edges(self):
        yield self.data[0]
        yield self.data[-1]
        yield ''.join(r[0] for r in self.data)
        yield ''.join(r[-1] for r in self.data)
        yield self.data[0][::-1]
        yield self.data[-1][::-1]
        yield ''.join(r[0] for r in self.data)[::-1]
        yield ''.join(r[-1] for r in self.data)[::-1]

    def get_data(self, rotation):
        data = self.data.copy()
        return rotate(data, rotation)

    def get_edge(self, rotation, edge):
        data = self.get_data(rotation)
        if edge == 't':
            return data[0]
        elif edge == 'b':
            return data[-1]
        elif edge == 'l':
            return ''.join(r[0] for r in data)
        elif edge == 'r':
            return ''.join(r[-1] for r in data)


def part1(a):
    return reduce(operator.mul, (t.id for t in a if sum(
        any(e == e2 for t2 in a for e2 in t2.get_edges() if t2.id != t.id) for e in t.get_edges()) == 4))


def part2(a):
    tiles = {t.id: t for t in a}

    # Create the grid with the ids
    neighbors = {t.id: {t2.id for t2 in a for e2 in t2.get_edges() for e in t.get_edges() if t2.id != t.id and e == e2}
                 for t in a}
    grid = [[None for _ in range(12)] for _ in range(12)]
    # first corner
    grid[0][0] = next(k for k, v in neighbors.items() if len(v) == 2)
    # first edge piece
    grid[0][1] = neighbors[grid[0][0]].pop()
    neighbors[grid[0][1]].remove(grid[0][0])
    # first row
    for i in range(2, 12):
        grid[0][i] = next(n for n in neighbors[grid[0][i - 1]] if len(neighbors[n]) <= 3)
        neighbors[grid[0][i - 1]].remove(grid[0][i])
        neighbors[grid[0][i]].remove(grid[0][i - 1])
    # rest of the grid
    for r in range(1, 12):
        for c in range(12):
            grid[r][c] = neighbors[grid[r - 1][c]].pop()
            neighbors[grid[r][c]].remove(grid[r - 1][c])
            if c != 0:
                neighbors[grid[r][c - 1]].remove(grid[r][c])
                neighbors[grid[r][c]].remove(grid[r][c - 1])

    # Rotate and flip the tiles
    # first corner
    rotations = {grid[0][0]: next(r for r in range(8) if
                                  tiles[grid[0][0]].get_edge(r, 'r') in tiles[grid[0][1]].get_edges()
                                  and tiles[grid[0][0]].get_edge(r, 'b') in tiles[grid[1][0]].get_edges())}
    # first row
    for i in range(1, 12):
        rotations[grid[0][i]] = next(r for r in range(8)
                                     if tiles[grid[0][i]].get_edge(r, 'l')
                                     == tiles[grid[0][i - 1]].get_edge(rotations[grid[0][i - 1]], 'r'))
    # rest of the grid
    for x in range(1, 12):
        for y in range(12):
            rotations[grid[x][y]] = next(r for r in range(8)
                                         if tiles[grid[x][y]].get_edge(r, 't')
                                         == tiles[grid[x - 1][y]].get_edge(rotations[grid[x - 1][y]], 'b'))
    # assemble picture
    tile_data = [[tiles[t].get_data(rotations[t]) for t in row] for row in grid]
    picture = [''.join(tile_data[row // 8][column // 8][row % 8 + 1][column % 8 + 1]
                       for column in range(12 * 8)) for row in range(12 * 8)]
    # count sea monsters
    sea_monster = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   "]

    def count_sea_monsters(picture):
        count = 0
        for r in range(len(picture)-len(sea_monster)+1):
            for c in range(len(picture[0])-len(sea_monster[0])+1):
                if all(sea_monster[i][j] == ' ' or picture[r+i][c+j] == '#'
                       for i in range(len(sea_monster)) for j in range(len(sea_monster[0]))):
                    count += 1
        return count

    sea_monsters = max(count_sea_monsters(rotate(picture, r)) for r in range(8))
    return sum(r.count('#') for r in picture) - sea_monsters*sum(r.count('#') for r in sea_monster)


if __name__ == '__main__':
    data = get_data(day=20, year=2020)
    inp = [Tile.parse_input(s) for s in data.split('\n\n')]
    print(part1(inp))
    print(part2(inp))
