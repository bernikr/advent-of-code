from collections.abc import Callable, Iterable
from typing import Any, Concatenate

from frozendict import frozendict

NO_EXTRA: dict[str, Any] = frozendict()  # type: ignore[assignment]


# "aocd" is needed as part of function name so that the aocd day/year detection works
def aocd_run_solver(
    solve: Callable[Concatenate[str, ...], Iterable[tuple[int, str | int]]],
) -> None:
    from aocd import AocdError, puzzle, submit  # noqa: PLC0415

    try:
        for i, example in enumerate(puzzle.examples, 1):
            solver = solve(example.input_data) if example.extra is None else solve(example.input_data, example.extra)
            for part, solution in solver:
                if example.answers[part - 1] is None:
                    continue
                if str(solution) == example.answers[part - 1]:
                    print(f"✔️  Example {i} part {part} passed with solution: {solution}")
                else:
                    print(f"❌ Example {i} part {part} failed: expected {example.answers[part - 1]}, got {solution}")
        for part, solution in solve(puzzle.input_data):
            submit(solution, part=("a", "b")[part - 1], day=puzzle.day, year=puzzle.year)
    except AocdError as e:
        print(e)
