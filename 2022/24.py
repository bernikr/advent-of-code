from functools import cache

from aoc_utils import Vec, PriorityQueue
from aocd import submit, AocdError, data

dirs = {
    ">": Vec(1, 0),
    "<": Vec(-1, 0),
    "^": Vec(0, -1),
    "v": Vec(0, 1)
}


def solve(inp, part1):
    inp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    mapp = {pos for pos, c in inp.items() if c != '#'}
    blizzards_initial = [(pos, dirs[c]) for pos, c in inp.items() if c in dirs]
    xmax, ymax = map(max, zip(*inp))

    @cache
    def _get_blizzards(time):
        if time == 0:
            return blizzards_initial
        prev = _get_blizzards(time - 1)
        blz = []
        for pos, dir in prev:
            newpos = pos + dir
            if newpos not in mapp:
                match dir:
                    case (1, 0):
                        newpos = Vec(1, newpos[1])
                    case (-1, 0):
                        newpos = Vec(xmax - 1, newpos[1])
                    case (0, 1):
                        newpos = Vec(newpos[0], 1)
                    case (0, -1):
                        newpos = Vec(newpos[0], ymax - 1)
            blz.append((newpos, dir))
        return blz

    @cache
    def get_blizzards(time):
        return {pos for pos, _ in _get_blizzards(time)}

    mvs = [Vec(0, 0), Vec(1, 0), Vec(-1, 0), Vec(0, 1), Vec(0, -1)]

    def find_path(start, target, startmove=1):
        q = PriorityQueue()
        seen = set()
        q.put((start, startmove), 0)
        while q:
            pos, move = q.get()
            if (pos, move) in seen:
                continue
            seen.add((pos, move))
            for d in mvs:
                newpos = pos + d
                if newpos == target:
                    return move
                if newpos in mapp and newpos not in get_blizzards(move):
                    q.put((newpos, move + 1), move + (newpos - target).manhatten())

    start = Vec(1, 0)
    target = Vec(xmax - 1, ymax)
    moves = find_path(start, target)
    if part1:
        return moves
    moves = find_path(target, start, moves + 1)
    moves = find_path(start, target, moves + 1)
    return moves


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
