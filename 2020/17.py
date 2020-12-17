import itertools

from aocd import get_data


def neighbors3d(x, y, z):
    return ((x+i, y+j, z+k) for i, j, k in itertools.product([-1, 0, 1], repeat=3) if not (i == 0 and j == 0 and k == 0))


def part1(a):
    active = set()
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] == '#':
                active.add((x, y, 0))
    for i in range(6):
        next = set()
        for x in range(min(c[0] for c in active)-1, max(c[0] for c in active)+2):
            for y in range(min(c[1] for c in active)-1, max(c[1] for c in active)+2):
                for z in range(min(c[2] for c in active)-1, max(c[2] for c in active)+2):
                    num = sum((a, b, c) in active for a, b, c in neighbors3d(x, y, z))
                    if ((x, y, z) in active and 2 <= num <= 3) or ((x, y, z) not in active and num == 3):
                        next.add((x, y, z))
        active = next
    return len(active)


def neighbors4d(x, y, z, w):
    return ((x+i, y+j, z+k, w+l) for i, j, k, l in itertools.product([-1, 0, 1], repeat=4) if not (i == 0 and j == 0 and k == 0 and l == 0))


def part2(a):
    active = set()
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] == '#':
                active.add((x, y, 0, 0))
    for i in range(6):
        next = set()
        for x in range(min(c[0] for c in active)-1, max(c[0] for c in active)+2):
            for y in range(min(c[1] for c in active)-1, max(c[1] for c in active)+2):
                for z in range(min(c[2] for c in active)-1, max(c[2] for c in active)+2):
                    for w in range(min(c[3] for c in active)-1, max(c[3] for c in active)+2):
                        num = sum((a, b, c, d) in active for a, b, c, d in neighbors4d(x, y, z, w))
                        if ((x, y, z, w) in active and 2 <= num <= 3) or ((x, y, z, w) not in active and num == 3):
                            next.add((x, y, z, w))
        active = next
    return len(active)


if __name__ == '__main__':
    data = get_data(day=17, year=2020)
    input = data.splitlines()
    print(part1(input))
    print(part2(input))
