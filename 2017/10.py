from aoc_utils import CircularList


def part1(inp):
    inp = [int(x) for x in inp.split(',')]
    l = CircularList(list(range(256)))
    pos, skip = 0, 0
    for length in inp:
        l[pos:pos + length] = l[pos + length - 1:pos - 1:-1]
        pos += length + skip
        skip += 1
    return l[0] * l[1]


def part2(inp):
    inp = [ord(x) for x in inp] + [17, 31, 73, 47, 23]
    l = CircularList(list(range(256)))
    pos, skip = 0, 0
    for _ in range(64):
        for length in inp:
            l[pos:pos + length] = l[pos + length - 1:pos - 1:-1]
            pos += length + skip
            skip += 1
    dense = [0 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            dense[i] ^= l[i * 16 + j]
    return ''.join(format(x, '02x') for x in dense)


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
