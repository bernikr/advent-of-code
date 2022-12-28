import re


def part1(a):
    def contains(rules, outer, inner):
        return outer == inner or any(contains(rules, i, inner) for _, i in rules[outer])

    return sum(contains(a, i, 'shiny gold') for i in a.keys()) - 1


def part2(a):
    def number_of_bags(rules, bag):
        return 1 + sum(int(n) * number_of_bags(rules, b) for n, b in rules[bag])

    return number_of_bags(a, 'shiny gold') - 1


def solve(inp, ispart1):
    inp = {l.split(' bags contain ')[0]: re.findall(r'(\d+) (\w+ \w+) bags?[,.]', l.split(' bags contain ')[1])
           for l in inp.splitlines()}
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
