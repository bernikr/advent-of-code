def react(p):
    diff = abs(ord('A') - ord('a'))

    poly = list(p)
    changed = True
    while changed:
        changed = False
        for i in range(0, len(poly) - 1):
            if poly[i] != '-' and abs(ord(poly[i]) - ord(poly[i + 1])) == diff:
                poly[i] = '-'
                poly[i + 1] = '-'
                changed = True
        poly = [x for x in poly if x != '-']
    return poly


def part1(a):
    return len(react(a))


def part2(a):
    return min(len(react([x for x in a if x != e1 and x != e2]))
               for e1, e2 in set((e, chr(ord(e) + 32)) for e in a if ord('A') <= ord(e) <= ord('Z')))


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
