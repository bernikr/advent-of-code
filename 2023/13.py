def find_reflection(pattern, diff=0):
    xmax, ymax = map(max, zip(*pattern.keys()))
    for i in range(1, xmax):
        if diff == sum(pattern[(x, y)] != pattern[(2 * i + 1 - x, y)]
                       for y in range(1, ymax + 1) for x in range(max(1, 2 * i + 1 - xmax), i + 1)):
            return i
    for i in range(1, ymax):
        if diff == sum(pattern[(x, y)] != pattern[(x, 2 * i + 1 - y)]
                       for x in range(1, xmax + 1) for y in range(max(1, 2 * i + 1 - ymax), i + 1)):
            return i * 100
    assert False


def solve(inp, part1):
    inp = [{(x, y): c for y, l in enumerate(p.splitlines(), 1) for x, c in enumerate(l, 1)}
           for p in inp.split("\n\n")]
    return sum(find_reflection(p, 0 if part1 else 1) for p in inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
