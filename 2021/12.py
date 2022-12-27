from itertools import chain, groupby
from operator import itemgetter


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


def solve(inp, ispart1):
    inp = {k: list(map(itemgetter(1), v))
           for k, v in groupby(
            sorted(chain.from_iterable([(a, b), (b, a)]
                                       for a, b in map(lambda x: x.split('-'), inp.splitlines()))), itemgetter(0))}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
