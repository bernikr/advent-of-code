from collections import defaultdict

from aocd import get_data


def run(a, limit):
    d = defaultdict(list)
    lastnum = 0
    for i in range(1, limit+1):
        if i <= len(a):
            d[a[i-1]].append(i)
            lastnum = a[i-1]
        else:
            if len(d[lastnum]) < 2:
                lastnum = 0
            else:
                lastnum = i-1-d[lastnum][-2]
            d[lastnum].append(i)
    return lastnum


def part1(a):
    return run(a, 2020)


def part2(a):
    return run(a, 30000000)


if __name__ == '__main__':
    data = get_data(day=15, year=2020)
    input = [int(i) for i in data.split(',')]
    print(part1(input))
    print(part2(input))
