import re


def coord_to_ord(x, y):
    return (x + y - 1) * (x + y) // 2 - y + 1


def solve(inp, _):
    inp = tuple(map(int, re.findall(r"\d+", inp)))
    code = 20151125
    for _ in range(coord_to_ord(inp[1], inp[0]) - 1):
        code = (code * 252533) % 33554393
    return code


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
    except AocdError as e:
        print(e)
