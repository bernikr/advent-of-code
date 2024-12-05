import importlib
import inspect


def solve(year: int, day: int, data: str) -> tuple:
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
