from aoc_utils import Vec
from tqdm import tqdm


def generate_bridges(parts, port=0, prev=Vec(0, 0)):
    for p in parts:
        if port not in p:
            continue
        new_port = p[0] if p[1] == port else p[1]
        yield prev + (1, sum(p))
        yield from generate_bridges(parts - {p}, port=new_port, prev=prev + (1, sum(p)))


def solve(inp, part1):
    parts = {tuple(map(int, l.split("/"))) for l in inp.splitlines()}
    key = (lambda x: x[1]) if part1 else (lambda x: x)
    return max(tqdm(generate_bridges(parts)), key=key)[1]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
