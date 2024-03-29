from collections import defaultdict
from enum import Enum
from itertools import chain

from aoc_utils import ocr


def get_parameter_address(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10 ** (n - 1)) % 10
    match flag:
        case 0:
            return p[ip + n]
        case 1:
            assert False, "Invalid use of immediate flag"
        case 2:
            return p[ip + n] + base
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def get_parameter(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10 ** (n - 1)) % 10
    match flag:
        case 0 | 2:
            return p[get_parameter_address(p, ip, base, n)]
        case 1:
            return p[ip + n]
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def execute(p, inp):
    inp = chain(inp)
    p = defaultdict(lambda: 0, {k: v for k, v in enumerate(p)})
    ip = 0
    base = 0
    while True:
        match p[ip] % 100:
            case 1:
                p[get_parameter_address(p, ip, base, 3)] = get_parameter(p, ip, base, 1) + get_parameter(p, ip, base, 2)
                ip += 4
            case 2:
                p[get_parameter_address(p, ip, base, 3)] = get_parameter(p, ip, base, 1) * get_parameter(p, ip, base, 2)
                ip += 4
            case 3:
                p[get_parameter_address(p, ip, base, 1)] = next(inp)
                ip += 2
            case 4:
                yield get_parameter(p, ip, base, 1)
                ip += 2
            case 5:
                if get_parameter(p, ip, base, 1) != 0:
                    ip = get_parameter(p, ip, base, 2)
                else:
                    ip += 3
            case 6:
                if get_parameter(p, ip, base, 1) == 0:
                    ip = get_parameter(p, ip, base, 2)
                else:
                    ip += 3
            case 7:
                p[get_parameter_address(p, ip, base, 3)] = 1 if get_parameter(p, ip, base, 1) < get_parameter(p, ip,
                                                                                                              base,
                                                                                                              2) else 0
                ip += 4
            case 8:
                p[get_parameter_address(p, ip, base, 3)] = 1 if get_parameter(p, ip, base, 1) == get_parameter(p, ip,
                                                                                                               base,
                                                                                                               2) else 0
                ip += 4
            case 9:
                base += get_parameter(p, ip, base, 1)
                ip += 2
            case 99:
                break
            case i:
                assert False, f"Instruction {i} not implemented yet"


class Dir(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def turn_left(self):
        return Dir((self.value[1], -self.value[0]))

    def turn_right(self):
        return Dir((-self.value[1], self.value[0]))


def part1(a):
    p = a.copy()

    panels = defaultdict(lambda: 0)
    pos = (0, 0)
    dir = Dir.UP

    def panel_gen():
        while True:
            yield panels[pos]

    robot = execute(p, panel_gen())
    while True:
        try:
            color = next(robot)
        except StopIteration:
            break
        turn = next(robot)

        panels[pos] = color

        if turn == 0:
            dir = dir.turn_left()
        else:
            dir = dir.turn_right()
        pos = (pos[0] + dir.value[0], pos[1] + dir.value[1])
    return len(panels)


def part2(a):
    p = a.copy()

    panels = defaultdict(lambda: 0)
    pos = (0, 0)
    panels[pos] = 1
    dir = Dir.UP

    def panel_gen():
        while True:
            yield panels[pos]

    robot = execute(p, panel_gen())
    while True:
        try:
            color = next(robot)
        except StopIteration:
            break
        turn = next(robot)

        panels[pos] = color

        if turn == 0:
            dir = dir.turn_left()
        else:
            dir = dir.turn_right()
        pos = (pos[0] + dir.value[0], pos[1] + dir.value[1])
    return ocr({(x - 1, y) for (x, y), v in panels.items() if v})


def solve(inp, ispart1):
    inp = list(map(int, inp.split(',')))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
