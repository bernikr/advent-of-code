from aocd import get_data


def part1(inp):
    buf = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + inp) % len(buf) + 1
        buf.insert(pos, i)
    return buf[(buf.index(2017) + 1) % len(buf)]


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=17, year=2017)
    inp = int(data)
    print(part1(inp))
    print(part2(inp))
