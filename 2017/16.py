import re

from aocd import get_data


def part1(inp):
    l = [chr(ord('a') + i) for i in range(16)]
    for ins in inp:
        if res := re.match(r'^s(\d+)', ins):
            a = int(res.group(1))
            l = l[-a:] + l[:-a]
        elif res := re.match(r'^x(\d+)/(\d+)', ins):
            a, b = map(int, res.groups())
            l[a], l[b] = l[b], l[a]
        elif res := re.match(r'^p(\w)/(\w)', ins):
            a, b = res.groups()
            l = [a if c == b else b if c == a else c for c in l]
        else:
            raise NotImplementedError(ins)
    return ''.join(l)


def part2(inp):
    return None


if __name__ == '__main__':
    data = get_data(day=16, year=2017)
    inp = data.split(',')
    print(part1(inp))
    print(part2(inp))
