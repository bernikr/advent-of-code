from more_itertools import chunked


def solve1(inp):
    return sum(ord(i) - ord('a') + 1 if i >= 'a' else ord(i) - ord('A') + 27
               for i in (set(a).intersection(b).pop() for a, b in ((l[:len(l) // 2], l[len(l) // 2:]) for l in inp)))


def solve2(inp):
    return sum(ord(i) - ord('a') + 1 if i >= 'a' else ord(i) - ord('A') + 27
               for i in (set(a).intersection(b).intersection(c).pop() for a, b, c in chunked(inp, 3)))


def solve(inp, part1):
    inp = inp.splitlines()
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
