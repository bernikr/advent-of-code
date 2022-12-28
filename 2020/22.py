from collections import deque
from functools import lru_cache


def part1(a):
    deck1 = deque(a[0])
    deck2 = deque(a[1])
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    deck = list(deck1) + list(deck2)
    return sum((i + 1) * n for i, n in enumerate(reversed(deck)))


@lru_cache(maxsize=None)
def play_recursive(p1, p2):
    deck1 = deque(p1)
    deck2 = deque(p2)
    seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if (tuple(deck1), tuple(deck2)) in seen:
            return 1, -1
        seen.add((tuple(deck1), tuple(deck2)))

        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 <= len(deck1) and card2 <= len(deck2):
            winner, _ = play_recursive(tuple(list(deck1)[:card1]), tuple(list(deck2)[:card2]))
        elif card1 > card2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    deck = list(deck1) + list(deck2)
    return 1 if len(deck1) > 0 else 2, sum((i + 1) * n for i, n in enumerate(reversed(deck)))


def part2(a):
    return play_recursive(tuple(a[0]), tuple(a[1]))[1]


def solve(inp, ispart1):
    inp = [[int(l) for l in p.splitlines()[1:]] for p in inp.split('\n\n')]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
