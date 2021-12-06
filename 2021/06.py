from collections import Counter, defaultdict

from aocd import get_data


def simulate(fish, iterations):
    for _ in range(iterations):
        nf = defaultdict(lambda: 0)
        for age, num in fish.items():
            if age > 0:
                nf[age - 1] += num
            else:
                nf[6] += num
                nf[8] += num
        fish = nf
    return fish


def part1(inp):
    return sum(simulate(inp, 80).values())


def part2(inp):
    return sum(simulate(inp, 256).values())


if __name__ == '__main__':
    data = get_data(day=6, year=2021)
    inp = dict(Counter(int(i) for i in data.split(',')))
    print(part1(inp))
    print(part2(inp))
