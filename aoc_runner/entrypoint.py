import importlib
import time


def solve(year, day, data):
    mod_name = f"{year}.{day:02}"
    mod = importlib.import_module(mod_name)
    t1 = time.perf_counter()
    a = mod.solve(data, True)
    t2 = time.perf_counter()
    b = mod.solve(data, False)
    t3 = time.perf_counter()
    # print(f"\n{year}.{day:02}, {(t2 - t1)*1000:0.3f}ms, {(t3 - t2)*1000:0.3f}ms")
    return a, b
