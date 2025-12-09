from collections.abc import Callable, Iterable
from typing import Any

from aocd import AocdError, submit
from aocd.models import Puzzle
from frozendict import frozendict

NO_EXTRA: dict[str, Any] = frozendict()  # type: ignore[assignment]

type SolveFunc = (
    Callable[[str], Iterable[tuple[int, str | int]]] | Callable[[str, dict[str, Any]], Iterable[tuple[int, str | int]]]
)


# "aocd" is needed as part of function name so that the aocd day/year detection works
def aocd_run_solver(
    solve: SolveFunc,
    *,
    only_example: int = 0,
    skip_examples: bool = False,
) -> None:
    from aocd import puzzle  # noqa: PLC0415

    if not skip_examples:
        run_examples(solve, puzzle, only_example=only_example)
    if not only_example:
        try:
            for part, solution in solve(puzzle.input_data):  # type: ignore[call-arg]
                submit(solution, part=("a", "b")[part - 1], day=puzzle.day, year=puzzle.year)
        except AocdError as e:
            print(e)


def run_examples(
    solve: SolveFunc,
    puzzle: Puzzle,
    *,
    only_example: int = 0,
) -> None:
    for i, example in enumerate(puzzle.examples, 1):
        if only_example and i != only_example:
            continue
        if example.extra is not None:
            print(f"Example {i} has extra parameters: {example.extra}")
        solver = solve(example.input_data) if example.extra is None else solve(example.input_data, example.extra)  # type: ignore[call-arg]
        for part, solution in solver:
            if example.answers[part - 1] is None:
                continue
            if str(solution) == example.answers[part - 1]:
                print(f"✔️  Example {i} part {part} passed with solution: {solution}")
            else:
                print(f"❌ Example {i} part {part} failed: expected {example.answers[part - 1]}, got {solution}")
