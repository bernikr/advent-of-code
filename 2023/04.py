def solve(inp, part1):
    won = [len(set(a).intersection(b)) for a, b in
           (tuple(map(lambda a: [int(x) for x in a.split(' ') if x], l[10:].split('|'))) for l in inp.splitlines())]
    if part1:
        return sum(int(2 ** (i - 1)) for i in won)
    else:
        cards = [1] * len(won)
        for i in range(len(won)):
            for j in range(won[i]):
                cards[i+j+1] += cards[i]
        return sum(cards)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
