import re


def solve(inp, part1):
    inp = [re.match(r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$", l).groups()
           for l in inp.splitlines()]
    inp = [(a, int(b), int(c), int(d)) for a, b, c, d in inp]

    flying = {r[0]: True for r in inp}
    distance = {r[0]: 0 for r in inp}
    last_state_change = {r[0]: 0 for r in inp}
    points = {r[0]: 0 for r in inp}
    for i in range(1, 2503 + 1):
        for r in inp:
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
    if part1:
        return max(distance.values())
    else:
        return max(points.values())


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
