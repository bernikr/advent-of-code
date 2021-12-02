import sys
from collections import defaultdict
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


def ascii_execute(p, inp):
    prog = execute(p, (ord(x) for x in inp))
    for c in prog:
        if c > 255:
            print('\n', end='', file=sys.stderr)
            return c
        print(chr(c), end='', file=sys.stderr)


def part1(a):
    p = a.copy()
    prog = """NOT T T
    AND A T
    AND B T
    AND C T
    NOT T T
    AND D T
    OR T J
    WALK\n"""
    return ascii_execute(p, prog)


def part2(a):
    p = a.copy()
    prog = """NOT C J
    AND D J
    NOT H T
    NOT T T
    OR E T
    AND T J
    NOT A T
    OR T J
    NOT B T
    NOT T T
    OR E T
    NOT T T
    OR T J
    RUN\n"""
    return ascii_execute(p, prog)


if __name__ == '__main__':
    data = get_data(day=21, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
