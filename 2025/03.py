from collections.abc import Iterable


def max_jolts(bank: list[int], digits: int) -> int:
    if digits == 1:
        return max(bank)
    digit = max(bank[: -(digits - 1)])
    return (digit * int(10 ** (digits - 1))) + max_jolts(bank[bank.index(digit) + 1 :], digits - 1)


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inp: list[list[int]] = [list(map(int, l)) for l in inp.splitlines()]
    yield 1, sum(max_jolts(l, 2) for l in inp)
    yield 2, sum(max_jolts(l, 12) for l in inp)


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
