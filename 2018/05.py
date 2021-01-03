from aocd import get_data


def react(p):
    diff = abs(ord('A')-ord('a'))

    poly = list(p)
    changed = True
    while changed:
        changed = False
        for i in range(0, len(poly)-1):
            if poly[i] != '-' and abs(ord(poly[i])-ord(poly[i+1])) == diff:
                poly[i] = '-'
                poly[i+1] = '-'
                changed = True
        poly = [x for x in poly if x != '-']
    return poly


def part1(a):
    return len(react(a))


def part2(a):
    return min(len(react([x for x in a if x != e1 and x != e2]))
               for e1, e2 in set((e, chr(ord(e)+32)) for e in a if ord('A') <= ord(e) <= ord('Z')))


if __name__ == '__main__':
    data = get_data(day=5, year=2018)
    inp = data
    print(part1(inp))
    print(part2(inp))
