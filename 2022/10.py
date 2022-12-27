from aoc_utils import ocr


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


def solve1(inp):
    outputs = list(run(inp))
    return sum(i * outputs[i - 1] for i in [20, 60, 100, 140, 180, 220])


def solve2(inp):
    outputs = list(run(inp))
    disp = set()
    for i, x in enumerate(outputs):
        if i % 40 in [x - 1, x, x + 1]:
            disp.add((i % 40, i // 40))
    return ocr(disp)


def solve(inp, part1):
    inp = [tuple(l.split(' ')) for l in inp.splitlines()]
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
