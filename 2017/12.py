from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=12, year=2017)
    inp = {int(a): frozenset(map(int, b.split(', '))) for a, b in (l.split(' <-> ') for l in data.splitlines())}
    print(part1(inp))
    print(part2(inp))
