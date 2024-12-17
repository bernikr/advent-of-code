import re
from collections import deque
from collections.abc import Iterable


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    a, b, c, *program = map(int, re.findall(r"(\d+)", inp))
    yield 1, ",".join(map(str, run(a, b, c, program)))

    partials = deque([0])
    while partials:
        a = partials.popleft()
        l = (a.bit_length() - 1) // 3 + 2
        for i in range(8):
            na = a * 8 + i
            if na != 0 and run(na, b, c, program)[-l:] == program[-l:]:
                if l == len(program):
                    yield 2, na
                    return
                partials.append(na)


def run(a: int, b: int, c: int, program: list[int]) -> list[int]:  # noqa: C901
    res = []
    ip = 0
    while ip < len(program):
        ins, op = program[ip], program[ip + 1]
        ip += 2
        if ins in {0, 2, 5, 6, 7}:
            op = [0, 1, 2, 3, a, b, c][op]
        match ins:
            case 0:
                a >>= op
            case 1:
                b ^= op
            case 2:
                b = op & 7
            case 3:
                if a:
                    ip = op
            case 4:
                b ^= c
            case 5:
                res.append(op & 7)
            case 6:
                b = a >> op
            case 7:
                c = a >> op
    return res


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
