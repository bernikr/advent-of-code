import itertools

from aocd import get_data


def part1(a):
    return sum(sum(c in 'aeiou' for c in s) >= 3
               and any(s[i] == s[i + 1] for i in range(len(s) - 1))
               and not any(seq in s for seq in ['ab', 'cd', 'pq', 'xy']) for s in a)


def part2(a):
    return sum(any(
        s.find(a + b) != -1 and s.find(a + b, s.find(a + b) + 2) != -1 for a, b in itertools.product(set(s), repeat=2))
               and any(s[i] == s[i + 2] for i in range(len(s) - 2)) for s in a)


if __name__ == '__main__':
    data = get_data(day=5, year=2015)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
