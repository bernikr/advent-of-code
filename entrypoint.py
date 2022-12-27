import importlib


def solve(year, day, data):
    mod_name = f"{year}.{day:02}"
    mod = importlib.import_module(mod_name)
    a = mod.solve(data, True)
    b = mod.solve(data, False)
    return a, b
