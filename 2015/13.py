import itertools
import re


def solve(inp, part1):
    inp = [re.match(r"^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).", l).groups() for l in
           inp.splitlines()]
    rules = {(a, b): int(i) * (-1 if s == 'lose' else 1) for a, s, i, b in inp}
    if not part1:
        rules.update({(a, b): 0 for a, b in
                      itertools.chain.from_iterable(((a, 'me'), ('me', a)) for a in set(map(lambda x: x[0], rules)))})
    return max(
        sum(rules[(s[i], s[(i + 1) % len(s)])] + rules[(s[(i + 1) % len(s)], s[i])] for i in range(len(s))) for s in
        itertools.permutations(set(map(lambda x: x[0], rules))))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
