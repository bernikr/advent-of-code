def part1(inp):
    i = 0
    while any(a <= i <= b for a, b in inp):
        for a, b in inp:
            if a <= i <= b:
                i = b + 1
    return i


def part2(inp):
    i = 0
    valid = 0
    while i <= 4294967295:
        while any(a <= i <= b for a, b in inp):
            for a, b in inp:
                if a <= i <= b:
                    i = b + 1
        if i <= 4294967295:
            valid += 1
            i += 1
    return valid


def solve(inp, ispart1):
    inp = [tuple(map(int, l.split('-'))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
