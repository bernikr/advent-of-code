from aoc_utils import Vec, Dir
from aocd import get_data


def part1(mapp):
    pos = next(c for c, v in mapp.items() if c[1] == 0 and v == '|')
    d = Dir.DOWN
    res = ''
    while True:
        if c := mapp.get(pos + d.value, None):
            pass
        elif c := mapp.get(pos + d.turn_left().value, None):
            d = d.turn_left()
        elif c := mapp.get(pos + d.turn_right().value, None):
            d = d.turn_right()
        else:
            return res
        pos += d.value
        if c.isalpha():
            res += c


def part2(mapp):
    pos = next(c for c, v in mapp.items() if c[1] == 0 and v == '|')
    d = Dir.DOWN
    res = 1
    while True:
        if mapp.get(pos + d.value, None):
            pass
        elif mapp.get(pos + d.turn_left().value, None):
            d = d.turn_left()
        elif mapp.get(pos + d.turn_right().value, None):
            d = d.turn_right()
        else:
            return res
        pos += d.value
        res += 1


if __name__ == '__main__':
    data = get_data(day=19, year=2017)
    inp = {Vec(x, y): c for y, l in enumerate(data.splitlines()) for x, c in enumerate(l) if c != ' '}
    print(part1(inp))
    print(part2(inp))
