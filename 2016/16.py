from aocd import get_data


def generate_dragon_curve(a):
    while True:
        yield a
        b = a[::-1].replace('0', 't').replace('1', '0').replace('t', '1')
        a = a + '0' + b


def checksum(s):
    if len(s) % 2 == 1:
        return s
    return checksum(''.join('1' if a == b else '0' for a, b in zip(s[::2], s[1::2])))


def calculate_checksum_for_disk(inp, l):
    return checksum(next(s for s in generate_dragon_curve(inp) if len(s) >= l)[0:l])


def part1(inp):
    return calculate_checksum_for_disk(inp, 272)


def part2(inp):
    return calculate_checksum_for_disk(inp, 35651584)


if __name__ == '__main__':
    inp = get_data(day=16, year=2016)
    print(part1(inp))
    print(part2(inp))
