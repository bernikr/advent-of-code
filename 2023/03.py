from itertools import product

from aoc_utils import Vec, dirs8


def solve(inp, part1):
    numbers = []
    symbols = {}
    pos_to_number_index = {}
    for y, l in enumerate(inp.splitlines()):
        x = 0
        while x < len(l):
            if l[x].isdigit():
                coords = [Vec(x, y)]
                nx = x + 1
                while nx < len(l) and l[nx].isdigit():
                    coords.append(Vec(nx, y))
                    nx += 1
                for c in coords:
                    pos_to_number_index[c] = len(numbers)
                numbers.append((int(l[x:nx]), coords))
                x = nx - 1
            elif l[x] != ".":
                symbols[Vec(x, y)] = l[x]
            x += 1

    if part1:
        return sum(n for n, cs in numbers if any(c + dir in symbols for c, dir in product(cs, dirs8)))
    else:
        gears = [k for k, v in symbols.items() if v == "*"]
        adjecent = [[numbers[i][0] for i in
                     {pos_to_number_index[g + dir] for dir in dirs8 if g + dir in pos_to_number_index}] for g in gears]
        return sum(a[0] * a[1] for a in adjecent if len(a) == 2)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
