import operator
from collections import defaultdict, Counter
from enum import Enum
from itertools import chain

from aocd import get_data


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

    def turn_left(self):
        match self:
            case self.NORTH:
                return self.WEST
            case self.WEST:
                return self.SOUTH
            case self.SOUTH:
                return self.EAST
            case self.EAST:
                return self.NORTH

    def turn_right(self):
        match self:
            case self.NORTH:
                return self.EAST
            case self.EAST:
                return self.SOUTH
            case self.SOUTH:
                return self.WEST
            case self.WEST:
                return self.NORTH


def part1(a):
    p = a.copy()
    mapp = defaultdict(lambda: '.',
                       {(x, y): c for y, l in enumerate(''.join(map(chr, execute(p, []))).splitlines())
                        for x, c in enumerate(l)})
    return sum(x * y for x, y in mapp.copy() if mapp[(x, y)] == '#' and all(mapp[d.move((x, y))] == '#' for d in Dir))


# https://stackoverflow.com/a/11091393
def find_repeated_substring(a, times):
    for n in range(1, 20)[::-1]:
        substrings = [a[i:i + n] for i in range(len(a) - n + 1)]
        freqs = Counter(substrings)
        if freqs.most_common(1)[0][1] >= times:
            return freqs.most_common(1)[0][0]


def part2(a):
    p = a.copy()
    mapp = ''.join(map(chr, execute(p, [])))
    print(mapp)
    path = ["L"]  # start direction needs to be manually added to path and d
    d = Dir.WEST
    mov = 0
    mapp = defaultdict(lambda: '.',
                       {(x, y): c for y, l in enumerate(''.join(map(chr, execute(p, []))).splitlines())
                        for x, c in enumerate(l)})
    pos = next(c for c in mapp if mapp[c] in "<>^v")
    while True:
        if mapp[d.move(pos)] == '#':
            pos = d.move(pos)
            mov += 1
        else:
            path.append(str(mov))
            mov = 0
            if mapp[d.turn_left().move(pos)] == "#":
                d = d.turn_left()
                path.append("L")
            elif mapp[d.turn_right().move(pos)] == "#":
                d = d.turn_right()
                path.append("R")
            else:
                break
    path = ','.join(path)
    # integers in the repeated_substring method must be tweaked manually
    print(f"PATH: {path}")
    path = ',' + path + ','
    A = find_repeated_substring(path, 3)[1:-1]
    print(f"A: {A}")
    assert len(A) <= 20
    path = path.replace(A, "A")
    B = find_repeated_substring(path, 3)[1:-1]
    print(f"B: {B}")
    assert len(B) <= 20
    assert not any('A' == c for c in B)
    path = path.replace(B, "B")
    C = find_repeated_substring(path, 3)[1:-1]
    print(f"C: {C}")
    assert len(C) <= 20
    assert not any(c in ['A', 'B'] for c in B)
    path = path.replace(C, "C")
    path = path[1:-1]
    print(f"PATH: {path}")
    assert len(path) <= 20
    payload = f"{path}\n{A}\n{B}\n{C}\nn\n"
    p = a.copy()
    p[0] = 2
    return list(execute(p, map(ord, payload)))[-1]


if __name__ == '__main__':
    data = get_data(day=17, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))