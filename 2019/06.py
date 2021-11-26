from itertools import groupby, zip_longest, takewhile
from operator import itemgetter

from aocd import get_data


def build_tree(inp, root):
    if root not in inp:
        return {}
    return {i: build_tree(inp, i) for i in inp[root]}


def part1(a):
    a = {k: list(map(itemgetter(1), v)) for k, v in groupby(sorted(a), key=itemgetter(0))}
    a = {"COM": build_tree(a, "COM")}

    counts = {"COM": 0}
    def count_recursivly(root, name):
        for k, v in root.items():
            counts[k] = counts[name] + 1
            count_recursivly(v, k)

    count_recursivly(a["COM"], "COM")
    return sum(counts.values())


def part2(a):
    a = {k: v for v, k in a}

    def get_path(p, t):
        if t == "COM":
            return ["COM"]
        return [*get_path(p, p[t]), t]

    return len(get_path(a, "YOU")) + len(get_path(a, "SAN")) - 2 - 2*len(list(takewhile(lambda x: x[0] == x[1], zip_longest(get_path(a, "YOU"), get_path(a, "SAN")))))




if __name__ == '__main__':
    data = get_data(day=6, year=2019)
    inp = list(map(lambda x: tuple(x.split(')')), data.splitlines()))
    print(part1(inp))
    print(part2(inp))
