from itertools import combinations

from aocd import get_data


def part1(a):
    a = sorted(a)
    dif = [j-i for i, j in zip(a[:-1], a[1:])]
    dif.append(a[0])
    return dif.count(1)*(dif.count(3)+1)


def part2(a):
    a.append(0)
    a.append(max(a)+3)
    a = sorted(a)

    next_indices = [[i for i, y in enumerate(a) if x < y <= x+3] for x in a]
    possibilities = [0 for _ in next_indices]
    for i in range(len(next_indices)-1, -1, -1):
        if i == len(next_indices)-1:
            possibilities[i] = 1
        else:
            possibilities[i] = sum(possibilities[j] for j in next_indices[i])

    return possibilities[0]


if __name__ == '__main__':
    data = get_data(day=10, year=2020)
    input = [int(l) for l in data.splitlines()]
    print(part1(input))
    print(part2(input))
