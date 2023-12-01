from functools import reduce


def solve(inp, part1):
    if not part1:
        digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}
        inp = reduce(lambda a, kv: a.replace(*kv), ((k, k + v + k) for k, v in digits.items()), inp)
    return sum(map(lambda x: int(x[0] + x[-1]), ([c for c in l if c.isdigit()] for l in inp.splitlines())))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
