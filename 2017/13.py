from itertools import count


def part1(inp):
    sev = 0
    for l, c in inp.items():
        if l % ((c - 1) * 2) == 0:
            sev += l * c
    return sev


def is_caught(inp, delay):
    for l, c in inp.items():
        if (l + delay) % ((c - 1) * 2) == 0:
            return True
    return False


def part2(inp):
    for i in count():
        if not is_caught(inp, i):
            return i


def solve(inp, ispart1):
    inp = {int(a): int(b) for a, b in (l.split(': ') for l in inp.splitlines())}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
