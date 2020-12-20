import re

from aocd import get_data

ticker = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

truth = {l.split(': ')[0]: int(l.split(': ')[1]) for l in ticker.splitlines()}


def part1(a):
    for sue in a:
        if all(truth[k] == int(v) for k, v in sue[1].items()):
            return sue[0]


def part2(a):
    for sue in a:
        if all(truth[k] < int(v) if k in ['cats', 'trees']
               else truth[k] > int(v) if k in ['pomeranians', 'goldfish']
               else truth[k] == int(v) for k, v in sue[1].items()):
            return sue[0]


if __name__ == '__main__':
    data = get_data(day=16, year=2015)
    inp = [(re.match(r"Sue (\d+):", l).group(1), dict(re.findall(r"(\w+): (\d+)(?:,|$)", l))) for l in
           data.splitlines()]
    print(part1(inp))
    print(part2(inp))
