import re


def part1(a):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for c, l in a:
        for i in range(l[0], l[2] + 1):
            for j in range(l[1], l[3] + 1):
                if c == 'turn on':
                    lights[i][j] = True
                elif c == 'turn off':
                    lights[i][j] = False
                elif c == 'toggle':
                    lights[i][j] = not lights[i][j]
    return sum(sum(row) for row in lights)


def part2(a):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for c, l in a:
        for i in range(l[0], l[2] + 1):
            for j in range(l[1], l[3] + 1):
                if c == 'turn on':
                    lights[i][j] += 1
                elif c == 'turn off':
                    lights[i][j] = max(0, lights[i][j] - 1)
                elif c == 'toggle':
                    lights[i][j] += 2
    return sum(sum(row) for row in lights)


def solve(inp, ispart1):
    inp = [(re.match(r'turn on|turn off|toggle', l).group(0),
            tuple(map(int, re.findall(r'\d+', l)))) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
