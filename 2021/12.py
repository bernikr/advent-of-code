from itertools import chain, groupby
from operator import itemgetter

from aocd import get_data


def part1(inp):
    paths = [['start']]
    found = 0
    while paths:
        np = []
        for p in paths:
            for n in inp[p[-1]]:
                match n:
                    case 'end':
                        found += 1
                    case x if x.islower() and x in p:
                        pass
                    case _:
                        np.append(p + [n])
        paths = np
    return found


def path_visited_small_cave_twice(path):
    for i in range(len(path)):
        if path[i].islower() and path[i] in path[i + 1:]:
            return True
    return False


def part2(inp):
    paths = [['start']]
    found = 0
    while paths:
        np = []
        for p in paths:
            for n in inp[p[-1]]:
                match n:
                    case 'start':
                        pass
                    case 'end':
                        found += 1
                    case x if x.islower() and x in p and path_visited_small_cave_twice(p):
                        pass
                    case _:
                        np.append(p + [n])
        paths = np
    return found


if __name__ == '__main__':
    data = get_data(day=12, year=2021)
    inp = {k: list(map(itemgetter(1), v))
           for k, v in groupby(
            sorted(chain.from_iterable([(a, b), (b, a)]
                                       for a, b in map(lambda x: x.split('-'), data.splitlines()))), itemgetter(0))}
    print(part1(inp))
    print(part2(inp))
