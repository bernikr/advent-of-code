from collections import Counter
from functools import cmp_to_key


def get_hand_type(hand, joker=False):
    c = Counter(hand)
    if joker:
        joker_num = c['J']
        del c['J']
        c = sorted(c.values(), reverse=True)
        if c:
            c[0] += joker_num
        else:
            c = [5]
    else:
        c = sorted(c.values(), reverse=True)
    types = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5]
    ]
    return types.index(c)


def tie_break_value(hand, joker=False):
    if joker:
        cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    else:
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return sum(cards.index(c) * len(cards) ** p for p, c in enumerate(reversed(hand)))


def compare_hands(a, b, joker=False):
    type_a, type_b = get_hand_type(a, joker), get_hand_type(b, joker)
    if type_a - type_b != 0:
        return type_a - type_b
    return tie_break_value(a, joker) - tie_break_value(b, joker)


def solve(inp, part1):
    inp = [(card, int(bid)) for card, bid in (l.split() for l in inp.splitlines())]
    sorted_hands = sorted(inp, key=cmp_to_key(lambda a, b: compare_hands(a[0], b[0], joker=not part1)))
    return sum(bid * rank for rank, (_, bid) in enumerate(sorted_hands, 1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
