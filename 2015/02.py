def solve(inp, part1):
    inp = [tuple(map(int, l.split('x'))) for l in inp.splitlines()]
    if part1:
        return sum(2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l) for l, w, h in inp)
    else:
        return sum(2 * a + 2 * b + a * b * c for a, b, c in (sorted(s) for s in inp))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
