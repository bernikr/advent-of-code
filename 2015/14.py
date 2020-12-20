import re

from aocd import get_data


def part1(a):
    flying = {r[0]: True for r in a}
    distance = {r[0]: 0 for r in a}
    last_state_change = {r[0]: 0 for r in a}
    for i in range(1, 2503 + 1):
        for r in a:
            n = r[0]
            if flying[n]:
                distance[n] += r[1]
                if i - last_state_change[n] == r[2]:
                    flying[n] = False
                    last_state_change[n] = i
            else:
                if i - last_state_change[n] == r[3]:
                    flying[n] = True
                    last_state_change[n] = i

    return max(distance.values())


def part2(a):
    flying = {r[0]: True for r in a}
    distance = {r[0]: 0 for r in a}
    last_state_change = {r[0]: 0 for r in a}
    points = {r[0]: 0 for r in a}
    for i in range(1, 2503 + 1):
        for r in a:
            n = r[0]
            if flying[n]:
                distance[n] += r[1]
                if i - last_state_change[n] == r[2]:
                    flying[n] = False
                    last_state_change[n] = i
            else:
                if i - last_state_change[n] == r[3]:
                    flying[n] = True
                    last_state_change[n] = i
        for r in distance.keys():
            if distance[r] == max(distance.values()):
                points[r] += 1

    return max(points.values())


if __name__ == '__main__':
    data = get_data(day=14, year=2015)
    inp = [re.match(r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$", l).groups()
           for l in data.splitlines()]
    inp = [(a, int(b), int(c), int(d)) for a, b, c, d in inp]
    print(part1(inp))
    print(part2(inp))
