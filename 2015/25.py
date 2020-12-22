import re

from aocd import get_data


def coord_to_ord(x, y):
    return (x+y-1)*(x+y)//2-y+1


def part1(a):
    code = 20151125
    for _ in range(coord_to_ord(a[1], a[0])-1):
        code = (code * 252533) % 33554393
    return code


def part2(a):
    return None


if __name__ == '__main__':
    data = get_data(day=25, year=2015)
    inp = tuple(map(int, re.findall(r"\d+", data)))
    print(part1(inp))
    print(part2(inp))
