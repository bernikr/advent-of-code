import re


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
            decoded += encoded[m.end():m.end() + l] * t
            encoded = encoded[m.end() + l:]
    return decoded


def part1(a):
    return len(decode(a))


def calculate_length(s):
    m = re.search(r"\((\d+)x(\d+)\)", s)
    if m is None:
        return len(s)
    l, t = tuple(map(int, m.groups()))
    return m.start() + t * calculate_length(s[m.end():m.end() + l]) + calculate_length(s[m.end() + l:])


def part2(a):
    return calculate_length(a)


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
