import re

directions = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}


def distance(i):
    return sum(abs(a) for a in i)


def get_wire_locations(instructions):
    x, y = 0, 0
    wire = []
    for dir, num in instructions:
        dx, dy = directions[dir]
        for i in range(num):
            x += dx
            y += dy
            wire.append((x, y))
    return wire


def part1(a):
    return min(map(lambda x: sum(abs(i) for i in x),
                   set(get_wire_locations(a[0])).intersection(set(get_wire_locations(a[1])))))


def part2(a):
    wire1 = get_wire_locations(a[0])
    wire2 = get_wire_locations(a[1])
    return min(map(lambda x: wire1.index(x) + wire2.index(x) + 2, set(wire1).intersection(set(wire2))))


def solve(inp, ispart1):
    inp = tuple([tuple(map(lambda x: int(x) if x.isnumeric() else x, re.match(r'([RDLU])(\d+)', c).groups()))
                 for c in l.split(',')] for l in inp.splitlines())
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
