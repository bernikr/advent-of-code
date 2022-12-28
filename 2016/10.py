import operator
import re
from collections import defaultdict
from functools import reduce

p1 = ""


class Bot:
    def __init__(self, id, low, high, bots):
        self.id = id
        self.low = low
        self.high = high
        self.bots = bots
        self.saved_num = None

    def __repr__(self):
        return '<Bot id:"{}">'.format(self.id)

    def append(self, i):
        if self.saved_num is None:
            self.saved_num = i
        else:
            high = max(self.saved_num, i)
            low = min(self.saved_num, i)

            # part1
            if (high, low) == (61, 17):
                global p1
                p1 = self.id

            self.bots[self.low].append(low)
            self.bots[self.high].append(high)


def simulate(a):
    bots = defaultdict(list)
    for b in a['rules']:
        bots[b[0]] = Bot(*b, bots)
    for v, id in a['input']:
        bots[id].append(int(v))

    # part2
    return reduce(operator.mul, [bots['output {}'.format(i)][0] for i in range(3)])


def solve(inp, part1):
    inp = {"rules": re.findall(r"^(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)$", inp, re.MULTILINE),
           "input": re.findall(r"^value (\d+) goes to (\w+ \d+)$", inp, re.MULTILINE)}
    p2 = simulate(inp)
    if part1:
        global p1
        return p1[4:]
    else:
        return p2


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
