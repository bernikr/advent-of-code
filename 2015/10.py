from aocd import get_data


def look_and_say(s):
    out = ''
    char = s[0]
    count = 1
    for c in s[1:]:
        if c != char:
            out += str(count) + char
            char = c
            count = 1
        else:
            count += 1
    out += str(count) + char
    return out


def part1(a):
    seq = a
    for _ in range(40):
        seq = look_and_say(seq)
    return len(seq)


def part2(a):
    seq = a
    for _ in range(50):
        seq = look_and_say(seq)
    return len(seq)


if __name__ == '__main__':
    data = get_data(day=10, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
