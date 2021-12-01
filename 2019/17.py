import operator
from collections import defaultdict
from enum import Enum
from itertools import chain

from aocd import get_data


def get_parameter_address(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10**(n-1)) % 10
    match flag:
        case 0:
            return p[ip+n]
        case 1:
            assert False, "Invalid use of immediate flag"
        case 2:
            return p[ip+n]+base
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def get_parameter(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10**(n-1)) % 10
    match flag:
        case 0 | 2:
            return p[get_parameter_address(p, ip, base, n)]
        case 1:
            return p[ip+n]
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
                p[get_parameter_address(p, ip, base, 3)] = 1 if get_parameter(p, ip, base, 1) < get_parameter(p, ip, base, 2) else 0
                ip += 4
            case 8:
                p[get_parameter_address(p, ip, base, 3)] = 1 if get_parameter(p, ip, base, 1) == get_parameter(p, ip, base, 2) else 0
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
    mapp = defaultdict(lambda: '.',
                       {(x, y): c for y, l in enumerate(''.join(map(chr, execute(p, []))).splitlines())
                        for x, c in enumerate(l)})
    return sum(x*y for x, y in mapp.copy() if mapp[(x, y)] == '#' and all(mapp[d.move((x, y))] == '#' for d in Dir))


def part2(a):
    p = a.copy()
    return None


if __name__ == '__main__':
    data = get_data(day=17, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
