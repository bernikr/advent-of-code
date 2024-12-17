import re
from collections.abc import Iterable
from itertools import count

from tqdm import tqdm


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    a, b, c, *program = map(int, re.findall(r"(\d+)", inp))
    yield 1, run(a, b, c, program)
    for i in tqdm(count()):
        if res := run(i, b, c, program, expect_quine=True):
            print(i, res)
            if res == ",".join(map(str, program)):
                yield 2, i


def run(a: int, b: int, c: int, program: list[int], *, expect_quine: bool = False) -> str | None:  # noqa: C901
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
                if expect_quine and res != program[:len(res)]:
                    return None
            case 6:
                b = a >> op
            case 7:
                c = a >> op
    return ",".join(map(str, res))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
