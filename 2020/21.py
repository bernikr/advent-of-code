import itertools
import re
from functools import reduce

from aocd import get_data


def get_possible_ingredients(a):
    allergens = set(itertools.chain.from_iterable(l[1] for l in a))
    possible_ingredients = {}
    for allergen in allergens:
        possible_ingredients[allergen] = reduce(lambda x, y: x.intersection(y), (l[0] for l in a if allergen in l[1]))
    return possible_ingredients


def part1(a):
    allergen_ingredients = set(itertools.chain.from_iterable(get_possible_ingredients(a).values()))
    return sum(len(i.difference(allergen_ingredients)) for i, _ in a)


def part2(a):
    ingredients = {}
    for allergen, possible_ingredients in sorted(get_possible_ingredients(a).items(), key=lambda x: len(x[1])):
        ingredients[allergen] = possible_ingredients.difference(set(ingredients.values())).pop()
    return ','.join(i for _, i in sorted(ingredients.items(), key=lambda x: x[0]))


if __name__ == '__main__':
    data = get_data(day=21, year=2020)
    inp = [(set(l.split(' (')[0].split(' ')), set(re.findall(r"\w+(?=[,)])", l))) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
