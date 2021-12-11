from aocd import get_data


def is_trap(s):
    return s in ['^^.', '.^^', '^..', '..^']


def next_line(s):
    return ''.join('^' if is_trap(('.' + s + '.')[i:i + 3]) else '.' for i in range(len(s)))


def part1(inp):
    lines = [inp]
    for _ in range(40-1):
        lines.append(next_line(lines[-1]))
    return sum(c == '.' for l in lines for c in l)


def part2(inp):
    lines = [inp]
    for _ in range(400000-1):
        lines.append(next_line(lines[-1]))
    return sum(c == '.' for l in lines for c in l)


if __name__ == '__main__':
    inp = get_data(day=18, year=2016)
    print(part1(inp))
    print(part2(inp))
