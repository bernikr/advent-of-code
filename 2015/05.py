import itertools


def part1(a):
    return sum(sum(c in 'aeiou' for c in s) >= 3
               and any(s[i] == s[i + 1] for i in range(len(s) - 1))
               and not any(seq in s for seq in ['ab', 'cd', 'pq', 'xy']) for s in a)


def part2(a):
    return sum(any(
        s.find(a + b) != -1 and s.find(a + b, s.find(a + b) + 2) != -1 for a, b in itertools.product(set(s), repeat=2))
               and any(s[i] == s[i + 2] for i in range(len(s) - 2)) for s in a)


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
