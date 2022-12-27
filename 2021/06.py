from collections import Counter, defaultdict


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


def solve(inp, ispart1):
    inp = dict(Counter(int(i) for i in inp.split(',')))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
