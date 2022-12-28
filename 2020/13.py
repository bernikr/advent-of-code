import itertools
import math


def part1(a):
    first = next(
        itertools.chain.from_iterable(((t, l) for l in a[1] if t % l == 0) for t in range(a[0], a[0] + min(a[1]))))
    return (first[0] - a[0]) * first[1]


def lcm(x, y):
    return x * y // math.gcd(x, y)


def part2(a):
    a = [(i, int(n)) for i, n in enumerate(a[2]) if n != 'x']
    number = 0
    current_lcm = 1
    for i, n in a:
        for j in range(1, n + 1):
            if (number + current_lcm * j + i) % n == 0:
                number += current_lcm * j
                break
        current_lcm = lcm(current_lcm, n)
    return number


def solve(inp, ispart1):
    inp = inp.splitlines()
    inp = (int(inp[0]), [int(i) for i in inp[1].split(',') if i != 'x'], inp[1].split(','))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
