def part1(a):
    dir = 0
    x, y = 0, 0
    for d, n in a:
        if d == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

        if dir >= 2:
            n *= -1

        if dir % 2 == 0:
            x += n
        else:
            y += n

    return abs(x) + abs(y)


def part2(a):
    dir = 0
    x, y = 0, 0
    visited = {(0, 0)}
    for d, n in a:
        if d == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

        for _ in range(n):
            step = -1 if dir >= 2 else 1

            if dir % 2 == 0:
                x += step
            else:
                y += step
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))


def solve(inp, ispart1):
    inp = [(l[0], int(l[1:])) for l in inp.split(', ')]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
