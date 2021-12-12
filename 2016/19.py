import math

from aocd import get_data


def naive_simulation1(n):
    elfs = list(range(1, n + 1))
    i = 0
    while len(elfs) > 1:
        i = (i + 1) % len(elfs)
        del elfs[i]
    return elfs[0]


def calculate1(n):
    return (n - 2 ** math.floor(math.log2(n))) * 2 + 1


def part1(inp):
    # for i in range(1, 100):
    #    print(f"{i}: {naive_simulation1(i)} {calculate1(i)}")
    return calculate1(inp)


def naive_simulation2(n):
    elfs = list(range(1, n + 1))
    i = 0
    while len(elfs) > 1:
        del elfs[(i + len(elfs)//2) % len(elfs)]
        i = (i + (0 if (i + len(elfs)//2) % len(elfs) < i else 1)) % len(elfs)
    return elfs[0]


def part2(inp):
    for i in range(1, 100):
        print(f"{i}: {naive_simulation2(i)}")


if __name__ == '__main__':
    data = get_data(day=19, year=2016)
    inp = int(data)
    print(part1(inp))
    print(part2(inp))
