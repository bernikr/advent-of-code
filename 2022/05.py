import re
from collections import deque
from itertools import count


def solve1(inp):
    stacks, ins = inp
    stacks = [s.copy() for s in stacks]
    for n, f, t in ins:
        for _ in range(n):
            stacks[t - 1].append(stacks[f - 1].pop())
    return ''.join(s[-1] for s in stacks)


def solve2(inp):
    stacks, ins = inp
    stacks = [s.copy() for s in stacks]
    for n, f, t in ins:
        stacks[t - 1] += stacks[f - 1][-n:]
        stacks[f - 1] = stacks[f - 1][:-n]
    return ''.join(s[-1] for s in stacks)


def solve(inp, part1):
    inp = inp.splitlines()
    stacks = [deque() for _ in range(len(inp[0]) // 4 + 1)]
    for i in count():
        if inp[i][1] == '1':
            break
        for j in range(1, len(inp[0]), 4):
            if inp[i][j] != ' ':
                stacks[j // 4].appendleft(inp[i][j])
    ins = [tuple(map(int, re.findall(r"\d+", m))) for m in inp[i + 2:]]
    inp = [list(s) for s in stacks], ins
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
