from aocd import get_data


def parse_line(l):
    if l.startswith("deal with increment "):
        return "inc", int(l[20:])
    if l.startswith("cut "):
        return "cut", int(l[4:])
    if l == "deal into new stack":
        return "new", None


def deal_new(cards):
    return list(reversed(cards))


def cut(cards, n):
    return cards[n:] + cards[:n]


def deal_inc(cards, n):
    res = [-1 for _ in cards]
    for i, c in enumerate(cards):
        res[(i * n) % len(cards)] = c
    return res


def part1(inp):
    deck = list(range(10007))
    for op, n in inp:
        if op == "cut":
            deck = cut(deck, n)
        if op == "inc":
            deck = deal_inc(deck, n)
        if op == "new":
            deck = deal_new(deck)
    return deck.index(2019)


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=22, year=2019)
    inp = [parse_line(l) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
