def part1(a):
    a = sorted(a)
    dif = [j - i for i, j in zip(a[:-1], a[1:])]
    dif.append(a[0])
    return dif.count(1) * (dif.count(3) + 1)


def part2(a):
    a.append(0)
    a.append(max(a) + 3)
    a = sorted(a)

    next_indices = [[i for i, y in enumerate(a) if x < y <= x + 3] for x in a]
    possibilities = [0 for _ in next_indices]
    for i in range(len(next_indices) - 1, -1, -1):
        if i == len(next_indices) - 1:
            possibilities[i] = 1
        else:
            possibilities[i] = sum(possibilities[j] for j in next_indices[i])

    return possibilities[0]


def solve(inp, ispart1):
    inp = [int(l) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
