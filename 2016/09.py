import re

from aocd import get_data


def decode(s):
    decoded = ''
    encoded = s
    while len(encoded) > 0:
        m = re.search(r"\((\d+)x(\d+)\)", encoded)
        if m is None:
            decoded += encoded
        else:
            l, t = tuple(map(int, m.groups()))
            decoded += encoded[:m.start()]
            decoded += encoded[m.end():m.end()+l]*t
            encoded = encoded[m.end()+l:]
    return decoded


def part1(a):
    return len(decode(a))


def calculate_length(s):
    m = re.search(r"\((\d+)x(\d+)\)", s)
    if m is None:
        return len(s)
    l, t = tuple(map(int, m.groups()))
    return m.start() + t*calculate_length(s[m.end():m.end()+l]) + calculate_length(s[m.end()+l:])


def part2(a):
    return calculate_length(a)


if __name__ == '__main__':
    data = get_data(day=9, year=2016)
    inp = data
    print(part1(inp))
    print(part2(inp))
