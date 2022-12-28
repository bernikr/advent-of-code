from itertools import combinations


def part1(a):
    return next(n for i, n in enumerate(a[25:]) if not any(x + y == n for x, y in combinations(a[i:25 + i], 2)))


def part2short(a):
    conset = next(a[i:j] for i, j in combinations(range(len(a) + 1), 2) if sum(a[i:j]) == 1639024365 and j > i + 1)
    return min(conset) + max(conset)


def part2efficient(a):
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 1639024365:
                return min(a[i:j + 1]) + max(a[i:j + 1])
            elif sum > 1639024365:
                break


def solve(inp, ispart1):
    inp = [int(l) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2efficient(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
