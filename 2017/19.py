from aoc_utils import Vec, Dir


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


def solve(inp, ispart1):
    inp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l) if c != ' '}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
