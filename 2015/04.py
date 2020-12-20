import hashlib

from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=4, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
