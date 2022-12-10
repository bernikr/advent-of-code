from itertools import count

from aoc_utils import ocr
from aocd import data, submit, AocdError


def run(prog):
    x = 1
    for ins in prog:
        match ins:
            case ("noop", ):
                yield x
            case ("addx", i):
                yield x
                yield x
                x += int(i)


def part1(inp):
    outputs = list(run(inp))
    return sum(i * outputs[i - 1] for i in [20, 60, 100, 140, 180, 220])


def part2(inp):
    outputs = list(run(inp))
    disp = set()
    for i, x in enumerate(outputs):
        if i % 40 in [x - 1, x, x + 1]:
            disp.add((i % 40, i // 40))
    return ocr(disp)


if __name__ == '__main__':
    inp = [tuple(l.split(' ')) for l in data.splitlines()]
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
