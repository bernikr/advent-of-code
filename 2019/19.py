from collections import defaultdict
from itertools import chain


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


def part1(a):
    p = a.copy()
    out = ""
    for y in range(50):
        for x in range(50):
            out += '#' if next(execute(p, [x, y])) else '.'
        out += '\n'
    return sum(c == '#' for c in out)


def part2(a):
    p = a.copy()
    pos = (0, 100)
    while True:
        if not next(execute(p, pos)):
            pos = (pos[0] + 1, pos[1])
        elif next(execute(p, (pos[0] + 99, pos[1] - 99))):
            return pos[0] * 10000 + pos[1] - 99
        else:
            pos = (pos[0], pos[1] + 1)


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
