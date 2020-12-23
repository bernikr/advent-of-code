import itertools
import re

from aocd import get_data


def contains_abba(s):
    return any(s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1] for i in range(len(s) - 3))


def supports_tls(addr):
    addr = [(i, contains_abba(s)) for i, s in addr]
    return any(b for i, b in addr if i % 2 == 0) and not any(b for i, b in addr if i % 2 == 1)


def part1(a):
    return sum(supports_tls(l) for l in a)


def find_abas(s):
    return [(s[i], s[i + 1]) for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i] != s[i + 1]]


def supports_ssl(addr):
    abas = set(itertools.chain.from_iterable(find_abas(b) for i, b in addr if i % 2 == 0))
    babs = set(itertools.chain.from_iterable(find_abas(b) for i, b in addr if i % 2 == 1))
    return len(abas.intersection({(b, a) for a, b in babs})) > 0


def part2(a):
    return sum(supports_ssl(l) for l in a)


if __name__ == '__main__':
    data = get_data(day=7, year=2016)
    inp = [list(enumerate(re.split(r"[\[\]]", l))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
