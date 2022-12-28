import json
import re


def part1(a):
    return sum(int(i) for i in re.findall(r"-?\d+", a))


def part2(a):
    def sum_without_red(obj):
        if isinstance(obj, dict):
            if any(v == 'red' for v in obj.values()):
                return 0
            else:
                return sum(map(sum_without_red, obj.values()))
        elif isinstance(obj, list):
            return sum(map(sum_without_red, obj))
        elif isinstance(obj, str):
            return 0
        elif isinstance(obj, int):
            return obj

    return sum_without_red(json.loads(a))


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
