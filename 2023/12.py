from functools import cache


@cache
def count_arrangements(row, sizes):
    if not sizes:
        if all(c in ".?" for c in row):
            return 1
        else:
            return 0
    if len(row) < sum(sizes):
        return 0
    res = 0
    if row[0] in ".?":
        res += count_arrangements(row[1:], sizes)
    if row[0] in "?#":
        if all(c in "?#" for c in row[:sizes[0]]) and (len(row) == sizes[0] or row[sizes[0]] in ".?"):
            res += count_arrangements(row[sizes[0] + 1:], sizes[1:])
    return res


def solve(inp, part1):
    inp = [(a, tuple(map(int, b.split(",")))) for a, b in map(lambda l: l.split(), inp.splitlines())]
    if not part1:
        inp = [("?".join([a] * 5), b * 5) for a, b in inp]
    return sum(count_arrangements(*l) for l in inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
