from aocd import get_data


def get_neighbors(x, y):
    return list(filter(lambda c: all(0 <= i < 5 for i in c), [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]))


def count_neighbors(mapp, x, y):
    return sum(mapp[c[1]*5+c[0]] == "#" for c in get_neighbors(x, y))


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
            return sum(2**n for n, c in enumerate(field) if c == '#')
        layouts.append(field)


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=24, year=2019)
    inp = ''.join(data.splitlines())
    print(part1(inp))
    print(part2(inp))
