import re

from aocd import get_data


def part1(a):
    def contains(rules, outer, inner):
        return outer == inner or any(contains(rules, i, inner) for _, i in rules[outer])
    return sum(contains(a, i, 'shiny gold') for i in a.keys())-1


def part2(a):
    def number_of_bags(rules, bag):
        return 1 + sum(int(n) * number_of_bags(rules, b) for n, b in rules[bag])
    return number_of_bags(a, 'shiny gold')-1


if __name__ == '__main__':
    data = get_data(day=7, year=2020)
    input = {l.split(' bags contain ')[0]: re.findall(r'(\d+) (\w+ \w+) bags?[,.]', l.split(' bags contain ')[1])
             for l in data.splitlines()}
    print(part1(input))
    print(part2(input))
