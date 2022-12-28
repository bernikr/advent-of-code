from tqdm import tqdm


def part1(inp):
    buf = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + inp) % len(buf) + 1
        buf.insert(pos, i)
    return buf[(buf.index(2017) + 1) % len(buf)]


def part2(inp):
    pos = 0
    last = 0
    length = 1
    for i in tqdm(range(50_000_000)):
        pos = (pos + inp) % length + 1
        length += 1
        if pos == 1:
            last = i + 1
    return last


def solve(inp, ispart1):
    inp = int(inp)
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
