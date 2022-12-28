def get_groups(inp):
    groups = set()
    for conn in (b.union({a}) for a, b in inp.items()):
        if any(g.intersection(conn) for g in groups):
            for old_group in (g for g in groups.copy() if g.intersection(conn)):
                groups.remove(old_group)
                conn = conn.union(old_group)
        groups.add(conn)
    return groups


def part1(inp):
    return next(len(g) for g in get_groups(inp) if 0 in g)


def part2(inp):
    return len(get_groups(inp))


def solve(inp, ispart1):
    inp = {int(a): frozenset(map(int, b.split(', '))) for a, b in (l.split(' <-> ') for l in inp.splitlines())}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
