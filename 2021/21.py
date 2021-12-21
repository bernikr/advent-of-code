from aocd import get_data


def deterministic_die():
    d = 1
    while True:
        yield d
        d = (d + 1) % 100
        d = d if d else 100


def part1(inp):
    p1pos, p2pos = inp
    p1score, p2score = 0, 0
    die = deterministic_die()
    d = 0
    while True:
        p1pos = (p1pos + sum(next(die) for _ in range(3))) % 10
        p1pos = p1pos if p1pos else 10
        p1score += p1pos
        d += 3
        if p1score >= 1000:
            break
        p2pos = (p2pos + sum(next(die) for _ in range(3))) % 10
        p2pos = p2pos if p2pos else 10
        p2score += p2pos
        d += 3
        if p2score >= 1000:
            break
    return min(p1score, p2score) * d


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=21, year=2021)
    inp = [int(l.split(' ')[-1]) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
