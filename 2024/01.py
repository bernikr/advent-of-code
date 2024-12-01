from collections import Counter

def solve(inp: str, part1: bool) -> str | int:
    inp = tuple(zip(*(map(int, l.split("   ")) for l in inp.splitlines())))
    if part1:
        return sum(abs(a - b) for a, b in zip(*map(sorted, inp)))
    else:
        return sum(Counter(inp[1])[i] * i for i in inp[0])


if __name__ == "__main__":
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
