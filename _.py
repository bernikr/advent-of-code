def solve(inp, part1):
    inp = inp.splitlines()
    print(inp)
    if part1:
        return None
    else:
        return None


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
