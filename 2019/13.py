from collections import defaultdict
from itertools import chain

import numpy as np


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


def part1(a):
    p = a.copy()
    game = execute(p, [])
    tiles = {}
    while True:
        try:
            x = next(game)
        except StopIteration:
            break
        y = next(game)
        t = next(game)
        tiles[(x, y)] = t
    return sum(1 for t in tiles.values() if t == 2)


def part2(a):
    p = a.copy()
    p[0] = 2
    tiles = defaultdict(lambda: 0)
    score = None

    TILES = {
        0: ' ',
        1: '#',
        2: 'x',
        3: '_',
        4: 'o'
    }

    class Input:
        def __iter__(self):
            return self

        def __next__(self):
            ## UNCOMMENT FOR VISUAL OUTPUT
            # print('\n'.join(''.join(TILES[tiles[(x, y)]] for x in range(max(t[0] for t in tiles)+1))
            #                 for y in range(max(t[1] for t in tiles)+1)))
            paddle = next(c[0] for c, t in tiles.items() if t == 3)
            ball = next(c[0] for c, t in tiles.items() if t == 4)
            return np.sign(ball - paddle)

    game = execute(p, Input())
    while True:
        try:
            x = next(game)
        except StopIteration:
            break
        y = next(game)
        t = next(game)
        if (x, y) == (-1, 0):
            score = t
        else:
            tiles[(x, y)] = t
    return score


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
