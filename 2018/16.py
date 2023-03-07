import re
from dataclasses import dataclass
from functools import reduce
from itertools import groupby
from operator import itemgetter


@dataclass
class Sample:
    before: tuple[int]
    ins: tuple[int]
    after: tuple[int]


ops = [
    lambda a, b, r: r[a] + r[b],  # addr
    lambda a, b, r: r[a] + b,  # addi
    lambda a, b, r: r[a] * r[b],  # mulr
    lambda a, b, r: r[a] * b,  # muli
    lambda a, b, r: r[a] & r[b],  # banr
    lambda a, b, r: r[a] & b,  # bani
    lambda a, b, r: r[a] | r[b],  # borr
    lambda a, b, r: r[a] | b,  # bori
    lambda a, b, r: r[a],  # setr
    lambda a, b, r: a,  # seti
    lambda a, b, r: 1 if a > r[b] else 0,  # gtir
    lambda a, b, r: 1 if r[a] > b else 0,  # gtri
    lambda a, b, r: 1 if r[a] > r[b] else 0,  # gtrr
    lambda a, b, r: 1 if a == r[b] else 0,  # eqir
    lambda a, b, r: 1 if r[a] == b else 0,  # eqri
    lambda a, b, r: 1 if r[a] == r[b] else 0,  # eqrr
]


def check_sample(sample):
    res = set()
    _, a, b, c = sample.ins
    for i in range(len(ops)):
        regs = list(sample.before)
        regs[c] = ops[i](a, b, regs)
        if tuple(regs) == sample.after:
            res.add(i)
    return res


def solve(inp, part1):
    samples, program = inp.split("\n\n\n\n")
    exp = re.compile(r"(\d+)[\s,]+(\d+)[\s,]+(\d+)[\s,]+(\d+)")
    samples = [Sample(*[tuple(map(int, r)) for r in exp.findall(s)]) for s in samples.split("\n\n")]
    program = [tuple(map(int, exp.match(l).groups())) for l in program.splitlines()]

    candidates = [(s.ins[0], check_sample(s)) for s in samples]
    if part1:
        return sum(1 for _, s in candidates if len(s) >= 3)
    candidates = {k: reduce(lambda a, b: a & b, map(itemgetter(1), v))
                  for k, v in groupby(sorted(candidates), itemgetter(0))}
    while any(len(c) > 1 for c in candidates.values()):
        solved = reduce(lambda a, b: a | b, (a for a in candidates.values() if len(a) == 1))
        candidates = {k: v - solved if len(v) > 1 else v for k, v in candidates.items()}
    op_map = {k: v.pop() for k, v in candidates.items()}

    regs = [0, 0, 0, 0]
    for op, a, b, c in program:
        regs[c] = ops[op_map[op]](a, b, regs)
    return regs[0]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
