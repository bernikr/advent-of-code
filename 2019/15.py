import operator
from collections import defaultdict
from enum import Enum
from itertools import chain


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
                p[get_parameter_address(p, ip, base, 3)] = \
                    1 if get_parameter(p, ip, base, 1) < get_parameter(p, ip, base, 2) else 0
                ip += 4
            case 8:
                p[get_parameter_address(p, ip, base, 3)] = \
                    1 if get_parameter(p, ip, base, 1) == get_parameter(p, ip, base, 2) else 0
                ip += 4
            case 9:
                base += get_parameter(p, ip, base, 1)
                ip += 2
            case 99:
                break
            case i:
                assert False, f"Instruction {i} not implemented yet"


class Dir(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def to_coords(self) -> tuple[int, int]:
        match self:
            case self.NORTH:
                return 0, -1
            case self.SOUTH:
                return 0, 1
            case self.EAST:
                return 1, 0
            case self.WEST:
                return -1, 0

    def move(self, c):
        return tuple(map(operator.add, c, self.to_coords()))

    def opposite(self):
        match self:
            case self.NORTH:
                return self.SOUTH
            case self.SOUTH:
                return self.NORTH
            case self.EAST:
                return self.WEST
            case self.WEST:
                return self.EAST


def part1(a):
    p = a.copy()
    commandqueue = []
    pos = (0, 0)
    mapp = defaultdict(lambda: -1, {(0, 0): 1})
    movstack: list[Dir] = []
    robot = execute(p, commandqueue)
    while True:
        if any(mapp[d.move(pos)] == -1 for d in Dir):
            for d in Dir:
                if mapp[d.move(pos)] != -1:
                    continue
                commandqueue.append(d.value)
                ret = next(robot)
                mapp[d.move(pos)] = ret
                if ret != 0:
                    movstack.append(d)
                    pos = d.move(pos)
                    if ret == 2:
                        return len(movstack)
                    break
        else:
            d = movstack.pop().opposite()
            commandqueue.append(d.value)
            pos = d.move(pos)
            _ = next(robot)


def part2(a):
    p = a.copy()
    commandqueue = []
    pos = (0, 0)
    mapp = defaultdict(lambda: -1, {(0, 0): 1})
    movstack: list[Dir] = []
    robot = execute(p, commandqueue)
    while True:
        if any(mapp[d.move(pos)] == -1 for d in Dir):
            for d in Dir:
                if mapp[d.move(pos)] != -1:
                    continue
                commandqueue.append(d.value)
                ret = next(robot)
                mapp[d.move(pos)] = ret
                if ret != 0:
                    movstack.append(d)
                    pos = d.move(pos)
                    break
        else:
            if not movstack:
                break
            d = movstack.pop().opposite()
            commandqueue.append(d.value)
            pos = d.move(pos)
            _ = next(robot)

    minutes = 0
    boundary = {k for k, v in mapp.items() if v == 2}
    while 1 in mapp.values():
        nb = set()
        for c in boundary:
            for d in Dir:
                nc = d.move(c)
                if mapp[nc] == 1:
                    mapp[nc] = 2
                    nb.add(nc)
        boundary = nb
        minutes += 1
    return minutes


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
