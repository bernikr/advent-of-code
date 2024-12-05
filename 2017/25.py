import re
from collections import defaultdict

from tqdm import tqdm

IN_STATE = re.compile(r"In state ([A-Z])")
WRITE_VAL = re.compile(r"Write the value ([01])")
MOVE = re.compile(r"Move one slot to the (left|right)")
NEW_STATE = re.compile(r"Continue with state ([A-Z])")


def parse_rule(r):
    state = IN_STATE.findall(r)[0]
    vals = map(int, WRITE_VAL.findall(r))
    moves = map(lambda x: {"left": -1, "right": 1}[x], MOVE.findall(r))
    new_states = NEW_STATE.findall(r)
    return state, tuple(zip(vals, moves, new_states))


def solve(inp):
    start, *rules = inp.split("\n\n")
    state = re.search(r"Begin in state ([A-Z])\.", start).group(1)
    steps = int(re.search(r"Perform a diagnostic checksum after (\d+) steps\.", start).group(1))
    rules = dict(parse_rule(r) for r in rules)
    tape = defaultdict(lambda: 0)
    cursor = 0
    for _ in tqdm(range(steps)):
        tape[cursor], move, state = rules[state][tape[cursor]]
        cursor += move
    return sum(tape.values())


if __name__ == '__main__':
    from aocd import AocdError, data, submit

    try:
        submit(solve(data), part="a")
    except AocdError as e:
        print(e)
