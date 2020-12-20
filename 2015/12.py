import json
import re

from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=12, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
