from tqdm import tqdm


def part1(inp):
    a, b = inp
    s = 0
    for _ in tqdm(range(40_000_000)):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a & 0b1111111111111111 == b & 0b1111111111111111:
            s += 1
    return s


def gen_a(a):
    while True:
        a = (a * 16807) % 2147483647
        if a & 0b11 == 0:
            yield a


def gen_b(b):
    while True:
        b = (b * 48271) % 2147483647
        if b & 0b111 == 0:
            yield b


def part2(inp):
    a, b = gen_a(inp[0]), gen_b(inp[1])
    s = 0
    for _ in tqdm(range(5_000_000)):
        if next(a) & 0b1111111111111111 == next(b) & 0b1111111111111111:
            s += 1
    return s


def solve(inp, ispart1):
    inp = [int(l.split(' ')[-1]) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
