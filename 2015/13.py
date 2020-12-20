import itertools
import re

from aocd import get_data


def calculate_happiness(rules):
    return max(
        sum(rules[(s[i], s[(i + 1) % len(s)])] + rules[(s[(i + 1) % len(s)], s[i])] for i in range(len(s))) for s in
        itertools.permutations(set(map(lambda x: x[0], rules))))


def part1(a):
    return calculate_happiness(a)


def part2(a):
    new_rules = a.copy()
    new_rules.update({(a, b): 0 for a, b in
                      itertools.chain.from_iterable(((a, 'me'), ('me', a)) for a in set(map(lambda x: x[0], a)))})
    return calculate_happiness(new_rules)


if __name__ == '__main__':
    data = get_data(day=13, year=2015)
    inp = [re.match(r"^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).", l).groups() for l in
           data.splitlines()]
    inp = {(a, b): int(i) * (-1 if s == 'lose' else 1) for a, s, i, b in inp}
    print(part1(inp))
    print(part2(inp))
