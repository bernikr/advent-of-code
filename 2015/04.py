import hashlib


def part1(a):
    i = 0
    while True:
        h = hashlib.md5((a + str(i)).encode()).hexdigest()
        if h.startswith('00000'):
            return i
        i += 1


def part2(a):
    i = 0
    while True:
        h = hashlib.md5((a + str(i)).encode()).hexdigest()
        if h.startswith('000000'):
            return i
        i += 1


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
