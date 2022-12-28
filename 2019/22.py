from itertools import chain


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


def simplify(ops, N=10007):
    nops = []
    for op, n in ops:
        if op != "new":
            nops.append((op, n))
        else:
            nops.append(("inc", N - 1))
            nops.append(("cut", 1))
    ops = nops
    while len(ops) > 2:
        nops = []
        i = 0
        while i < len(ops):
            if i == len(ops) - 1:
                nops.append(ops[i])
                i += 1
            else:
                a, an = ops[i]
                b, bn = ops[i + 1]
                if a == b == "cut":
                    nops.append(("cut", (an + bn) % N))
                    i += 2
                elif a == b == "inc":
                    nops.append(("inc", (an * bn) % N))
                    i += 2
                elif a == "cut" and b == "inc":
                    nops.append(("inc", bn))
                    nops.append(("cut", (an * bn) % N))
                    i += 2
                else:
                    nops.append((a, an))
                    i += 1
        ops = nops
    return ops


def create_multi_shuffle(ops, n, N=10007):
    n_bin = format(n, 'b')
    ops = simplify(ops, N=N)
    shuffle_powers = [[] for _ in n_bin]
    shuffle_powers[0] = ops
    for i in range(1, len(shuffle_powers)):
        shuffle_powers[i] = simplify(shuffle_powers[i - 1] * 2, N=N)
    return simplify(chain.from_iterable(shuffle_powers[i] for i, b in enumerate(reversed(n_bin)) if b == '1'), N=N)


def part2(inp):
    shuffles = 101741582076661
    deck_size = 119315717514047
    ops = inp.copy()
    ops = create_multi_shuffle(ops, shuffles, deck_size)
    assert len(ops) == 2
    return f"Wolfram Alpha this: `(x * {ops[0][1]}) - {ops[1][1]} = 2020 mod {deck_size}`"


def solve(inp, ispart1):
    inp = [parse_line(l) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
