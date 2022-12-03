from aocd import data, submit, AocdError
from more_itertools import chunked


def part1(inp):
    return sum(ord(i) - ord('a') + 1 if i >= 'a' else ord(i) - ord('A') + 27
               for i in (set(a).intersection(b).pop() for a, b in ((l[:len(l) // 2], l[len(l) // 2:]) for l in inp)))


def part2(inp):
    return sum(ord(i) - ord('a') + 1 if i >= 'a' else ord(i) - ord('A') + 27
               for i in (set(a).intersection(b).intersection(c).pop() for a, b, c in chunked(inp, 3)))


if __name__ == '__main__':
    inp = data.splitlines()
    try:
        submit(part1(inp), part="a")
        submit(part2(inp), part="b")
    except AocdError as e:
        print(e)
