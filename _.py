def solve(inp: str, part1: bool) -> str | int:
    inp = inp.splitlines()
    print(inp)
    if part1:
        return ""
    else:
        return ""


if __name__ == "__main__":
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
