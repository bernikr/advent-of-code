def solve(inp: str) -> str | int:
    inp = inp.splitlines()
    print(inp)
    yield 1, ""
    yield 2, ""


if __name__ == "__main__":
    from aocd import data, submit, AocdError

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
