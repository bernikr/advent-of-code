import operator
import re
from collections import defaultdict
from functools import reduce

from aocd import get_data


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

            #part1
            if (high, low) == (61, 17):
                print(self.id)

            self.bots[self.low].append(low)
            self.bots[self.high].append(high)


def simulate(a):
    bots = defaultdict(list)
    for b in a['rules']:
        bots[b[0]] = Bot(*b, bots)
    for v, id in a['input']:
        bots[id].append(int(v))

    #part2
    print(reduce(operator.mul, [bots['output {}'.format(i)][0] for i in range(3)]))


def part2(a):
    return None


if __name__ == '__main__':
    data = get_data(day=10, year=2016)
    inp = {"rules": re.findall(r"^(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)$", data, re.MULTILINE),
           "input": re.findall(r"^value (\d+) goes to (\w+ \d+)$", data, re.MULTILINE)}
    simulate(inp)
