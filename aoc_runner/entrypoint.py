import importlib
import inspect


def solve(year, day, data):
    mod_name = f"{year}.{day:02}"
    mod = importlib.import_module(mod_name)

    if len(inspect.signature(mod.solve).parameters) == 2:
        a = mod.solve(data, True)
        b = mod.solve(data, False)
        return a, b
    else:
        sol = [None, None]
        for part, solution in mod.solve(data):
            sol[part - 1] = solution
            if all(sol):
                return tuple(sol)
