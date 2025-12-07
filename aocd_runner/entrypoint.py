import contextlib
import importlib
import inspect
import io
import json
import os
import sys
from collections.abc import Generator


@contextlib.contextmanager
def no_output() -> Generator[None]:
    save_stdout = sys.stdout
    sys.stdout = io.StringIO()
    save_stderr = sys.stderr
    sys.stderr = io.StringIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr


def solve(year: int, day: int, data: str) -> tuple[str | int | None, str | int | None]:  # noqa: C901
    with no_output():
        mod_name = f"{year}.{day:02}"
        mod = importlib.import_module(mod_name)

        if (
            len(inspect.signature(mod.solve).parameters) == 2
            and inspect.signature(mod.solve).parameters.get("extra") is None
        ):
            try:
                a = mod.solve(data, True)  # noqa: FBT003
            except:  # noqa: E722
                a = None
            try:
                b = mod.solve(data, False)  # noqa: FBT003
            except:  # noqa: E722
                b = None
            return a, b
        if (
            len(inspect.signature(mod.solve).parameters) == 2
            and inspect.signature(mod.solve).parameters.get("extra") is not None
        ):
            sol = [None, None]
            try:
                extra = dict(json.loads(os.environ.get("AOCD_EXTRA", "{}")).items())
                for part, solution in mod.solve(data, extra):
                    sol[part - 1] = solution
                    if all(sol):
                        break
            except:  # noqa: E722, S110
                pass
            return tuple(sol)  # type: ignore[return-value]
        if len(inspect.signature(mod.solve).parameters) == 1:
            sol = [None, None]
            try:
                for part, solution in mod.solve(data):
                    sol[part - 1] = solution
                    if all(sol):
                        break
            except:  # noqa: E722, S110
                pass
            return tuple(sol)  # type: ignore[return-value]

    raise NotImplementedError
