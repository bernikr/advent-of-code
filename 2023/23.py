from itertools import pairwise
from operator import itemgetter

import networkx as nx

from aoc_utils import Vec, dirs4, UP, DOWN, LEFT, RIGHT

valid_dirs = {".": dirs4, "^": [UP], "v": [DOWN], "<": [LEFT], ">": [RIGHT], "#": []}


def simplify(g: nx.DiGraph):
    for n in list(g.nodes):
        if g.in_degree[n] == g.out_degree[n] == 2:
            a, b = g.pred[n], g.succ[n]
            if a == b:
                a, b = a
                g.add_edge(a, b, distance=g[a][n]["distance"] + g[n][b]["distance"])
                g.add_edge(b, a, distance=g[a][n]["distance"] + g[n][b]["distance"])
                g.remove_node(n)
        elif g.in_degree[n] == g.out_degree[n] == 1:
            a, b = next(iter(g.pred[n])), next(iter(g.succ[n]))
            if a != b:
                g.add_edge(a, b, distance=g[a][n]["distance"] + g[n][b]["distance"])
                g.remove_node(n)
        elif g.in_degree[n] == 2 and g.out_degree[n] == 1:
            a, b = set(g.pred[n]), next(iter(g.succ[n]))
            if b in a:
                a = next(iter(a - {b}))
                g.add_edge(a, b, distance=g[a][n]["distance"] + g[n][b]["distance"])
                g.remove_node(n)
        elif g.in_degree[n] == 1 and g.out_degree[n] == 2:
            a, b = next(iter(g.pred[n])), set(g.succ[n])
            if a in b:
                b = next(iter(b - {a}))
                g.add_edge(a, b, distance=g[a][n]["distance"] + g[n][b]["distance"])
                g.remove_node(n)


def solve(inp, part1):
    mapp = {Vec(x, y): c for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l)}
    start = next(p for p, c in mapp.items() if c == "." and p[1] == 0)
    ymax = max(map(itemgetter(1), mapp.keys()))
    end = next(p for p, c in mapp.items() if c == "." and p[1] == ymax)
    g = nx.DiGraph()
    for pos, c in mapp.items():
        for d in valid_dirs[c]:
            if mapp.get(pos + d, "#") != "#":
                g.add_edge(pos, pos + d, distance=1)
    simplify(g)
    if not part1:
        g = g.to_undirected()

    return max(sum(g[a][b]['distance'] for a, b in pairwise(path)) for path in nx.all_simple_paths(g, start, end))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
