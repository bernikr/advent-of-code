from collections import Counter

cards = '23456789TJQKA'

hand_type_1 = lambda x: sorted(Counter(x).values(), reverse=True)
hand_type_2 = lambda x: max(hand_type_1(x.replace('J', a)) for a in cards)

tie_break_1 = lambda x: [cards.index(c) for c in x]
tie_break_2 = lambda x: [('J' + cards).index(c) for c in x]


def solve(inp, part1):
    inp = [(card, int(bid)) for card, bid in (l.split() for l in inp.splitlines())]
    hand_type, tie_break = (hand_type_1, tie_break_1) if part1 else (hand_type_2, tie_break_2)
    sorted_hands = sorted(inp, key=lambda x: hand_type(x[0]) + tie_break(x[0]))
    return sum(bid * rank for rank, (_, bid) in enumerate(sorted_hands, 1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
