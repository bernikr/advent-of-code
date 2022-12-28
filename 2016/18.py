def is_trap(s):
    return s in ['^^.', '.^^', '^..', '..^']


def next_line(s):
    return ''.join('^' if is_trap(('.' + s + '.')[i:i + 3]) else '.' for i in range(len(s)))


def part1(inp):
    lines = [inp]
    for _ in range(40 - 1):
        lines.append(next_line(lines[-1]))
    return sum(c == '.' for l in lines for c in l)


def part2(inp):
    lines = [inp]
    for _ in range(400000 - 1):
        lines.append(next_line(lines[-1]))
    return sum(c == '.' for l in lines for c in l)


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
