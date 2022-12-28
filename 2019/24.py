from itertools import chain


def get_neighbors(x, y):
    return list(filter(lambda c: all(0 <= i < 5 for i in c), [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]))


def count_neighbors(mapp, x, y):
    return sum(mapp[c[1] * 5 + c[0]] == "#" for c in get_neighbors(x, y))


def part1(inp):
    field = inp
    layouts = [field]
    while True:
        nf = ""
        for i, f in enumerate(field):
            n = count_neighbors(field, i % 5, i // 5)
            if f == "#" and n != 1:
                nf += "."
            elif f == "." and n in [1, 2]:
                nf += "#"
            else:
                nf += f
        field = nf
        if field in layouts:
            return sum(2 ** n for n, c in enumerate(field) if c == '#')
        layouts.append(field)


def get_recursive_neighbors(x, y, d):
    neighbors = list(filter(lambda c: 0 <= c[0] < 5 and 0 <= c[1] < 5 and not c[:2] == (2, 2),
                            [(x - 1, y, d), (x + 1, y, d), (x, y - 1, d), (x, y + 1, d)]))
    if x == 0:
        neighbors.append((1, 2, d - 1))
    if x == 4:
        neighbors.append((3, 2, d - 1))
    if y == 0:
        neighbors.append((2, 1, d - 1))
    if y == 4:
        neighbors.append((2, 3, d - 1))
    if (x, y) == (2, 1):
        neighbors += [(i, 0, d + 1) for i in range(5)]
    if (x, y) == (2, 3):
        neighbors += [(i, 4, d + 1) for i in range(5)]
    if (x, y) == (1, 2):
        neighbors += [(0, i, d + 1) for i in range(5)]
    if (x, y) == (3, 2):
        neighbors += [(4, i, d + 1) for i in range(5)]
    return neighbors


def part2(inp):
    bugs = {(i % 5, i // 5, 0) for i, c in enumerate(inp) if c == '#'}
    for _ in range(200):
        poi = set(chain(chain.from_iterable(get_recursive_neighbors(*b) for b in bugs), bugs))
        nb = set()
        for p in poi:
            n = len(bugs.intersection(get_recursive_neighbors(*p)))
            if (p in bugs and n == 1) or (p not in bugs and n in [1, 2]):
                nb.add(p)
        bugs = nb
    return len(bugs)


def solve(inp, ispart1):
    inp = ''.join(inp.splitlines())
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
