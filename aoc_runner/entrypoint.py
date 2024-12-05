import contextlib
import importlib
import inspect
import io
import sys


@contextlib.contextmanager
def no_output():  # noqa: ANN201
    save_stdout = sys.stdout
    sys.stdout = io.StringIO()
    save_stderr = sys.stderr
    sys.stderr = io.StringIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr


def solve(year: int, day: int, data: str) -> tuple:
    with no_output():
        mod_name = f"{year}.{day:02}"
        mod = importlib.import_module(mod_name)

        if len(inspect.signature(mod.solve).parameters) == 2:
            a = mod.solve(data, True)  # noqa: FBT003
            b = mod.solve(data, False)  # noqa: FBT003
            return a, b
        if len(inspect.signature(mod.solve).parameters) == 1:
            sol = [None, None]
            for part, solution in mod.solve(data):
                sol[part - 1] = solution
                if all(sol):
                    return tuple(sol)

    raise NotImplementedError
