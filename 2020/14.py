import re

from aocd import get_data


def part1(a):
    ormask = 0
    andmask = ~0
    mem = {}
    for l in a:
        if l[0] == 'mask':
            ormask = int(l[2].replace('X', '0'), 2)
            andmask = int(l[2].replace('X', '1'), 2)
        if l[0] == 'mem':
            mem[int(l[1])] = int(l[2]) & andmask | ormask
    return sum(mem.values())


def part2(a):
    def decode_addr(addr, mask):
        addr = ''.join('1' if mb == '1' else ('X' if mb == 'X' else ab) for ab, mb in zip(format(addr, '036b'), mask))
        c = addr.count('X')
        for i in range(2 ** c):
            xvalues = format(i, '0{}b'.format(c))
            cur_addr = addr
            for x in xvalues:
                cur_addr = cur_addr.replace('X', x, 1)
            yield int(cur_addr, 2)

    mask = '0' * 36
    mem = {}
    for l in a:
        if l[0] == 'mask':
            mask = l[2]
        if l[0] == 'mem':
            for addr in decode_addr(int(l[1]), mask):
                mem[addr] = int(l[2])
    return sum(mem.values())


if __name__ == '__main__':
    data = get_data(day=14, year=2020)
    inp = [re.match(r'^(\w+)(?:\[(\d+)])? = ([\dX]+)$', l).groups() for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
