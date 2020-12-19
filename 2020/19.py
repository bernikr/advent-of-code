import re

from aocd import get_data
from regex import regex


def part1(a):
    def parse_rule(n):
        r = a[0][n].split(' ')
        r = ''.join('|' if t == '|' else t[1] if t[0] == '"' else parse_rule(int(t)) for t in r)
        if '|' in r:
            return '(?:' + r + ')'
        else:
            return r
    rule = re.compile('^' + parse_rule(0) + '$')
    return sum(1 if rule.match(l) is not None else 0 for l in a[1])


def part2(a):
    a[0][8] = '42 | 42 8'
    a[0][11] = '42 31 | 42 11 31'
    pattern = r"(?V1)(?(DEFINE){})^(?P>r0)$".format(''.join("(?<r{}>{})".format(k, ''.join('|' if t == '|' else t[1] if t[0] == '"' else '(?P>r{})'.format(t) for t in v.split(' '))) for k, v in a[0].items()))
    rule = regex.compile(pattern)
    return sum(1 if rule.match(l) is not None else 0 for l in a[1])


if __name__ == '__main__':
    data = get_data(day=19, year=2020)
    input = data.split('\n\n')
    input[0] = {int(l.split(':')[0]): l.split(': ')[1] for l in input[0].splitlines()}
    input[1] = input[1].splitlines()
    print(part1(input))
    print(part2(input))
