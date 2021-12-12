from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=20, year=2016)
    inp = [tuple(map(int, l.split('-'))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
