from aocd import get_data
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


if __name__ == '__main__':
    data = get_data(day=17, year=2017)
    inp = int(data)
    print(part1(inp))
    print(part2(inp))
