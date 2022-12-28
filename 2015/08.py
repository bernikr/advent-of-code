def solve(inp, part1):
    inp = inp.splitlines()
    if part1:
        return sum(len(l) - len(l.encode('utf-8').decode('unicode_escape')) + 2 for l in inp)
    else:
        return sum(len(l.encode('unicode_escape').decode('utf-8').replace('"', '\\"')) - len(l) + 2 for l in inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
