from itertools import combinations

from aocd import get_data


def part1(a):
    return next(n for i, n in enumerate(a[25:]) if not any(x + y == n for x, y in combinations(a[i:25 + i], 2)))


def part2short(a):
    conset = next(a[i:j] for i, j in combinations(range(len(a)+1), 2) if sum(a[i:j]) == 1639024365 and j > i+1)
    return min(conset)+max(conset)


def part2efficient(a):
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 1639024365:
                return min(a[i:j+1])+max(a[i:j+1])
            elif sum > 1639024365:
                break


if __name__ == '__main__':
    data = get_data(day=9, year=2020)
    inp = [int(l) for l in data.splitlines()]
    print(part1(inp))
    print(part2efficient(inp))
    print(part2short(inp))
