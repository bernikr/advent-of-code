from collections import defaultdict
from itertools import chain, cycle

from aocd import get_data


def get_parameter_address(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10**(n-1)) % 10
    match flag:
        case 0:
            return p[ip+n]
        case 1:
            assert False, "Invalid use of immediate flag"
        case 2:
            return p[ip+n]+base
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def get_parameter(p, ip, base, n):
    flags = p[ip] // 100
    flag = (flags // 10**(n-1)) % 10
    match flag:
        case 0 | 2:
            return p[get_parameter_address(p, ip, base, n)]
        case 1:
            return p[ip+n]
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def execute(p, inp):
    inp = chain(inp)
    p = defaultdict(lambda: 0, {k: v for k, v in enumerate(p)})
    ip = 0
    base = 0
    while True:
        match p[ip] % 100:
            case 1:
                p[get_parameter_address(p, ip, base, 3)] = get_parameter(p, ip, base, 1) + get_parameter(p, ip, base, 2)
                ip += 4
            case 2:
                p[get_parameter_address(p, ip, base, 3)] = get_parameter(p, ip, base, 1) * get_parameter(p, ip, base, 2)
                ip += 4
            case 3:
                yield None
                p[get_parameter_address(p, ip, base, 1)] = next(inp)
                ip += 2
            case 4:
                yield get_parameter(p, ip, base, 1)
                ip += 2
            case 5:
                if get_parameter(p, ip, base, 1) != 0:
                    ip = get_parameter(p, ip, base, 2)
                else:
                    ip += 3
            case 6:
                if get_parameter(p, ip, base, 1) == 0:
                    ip = get_parameter(p, ip, base, 2)
                else:
                    ip += 3
            case 7:
                p[get_parameter_address(p, ip, base, 3)] = \
                    1 if get_parameter(p, ip, base, 1) < get_parameter(p, ip, base, 2) else 0
                ip += 4
            case 8:
                p[get_parameter_address(p, ip, base, 3)] = \
                    1 if get_parameter(p, ip, base, 1) == get_parameter(p, ip, base, 2) else 0
                ip += 4
            case 9:
                base += get_parameter(p, ip, base, 1)
                ip += 2
            case 99:
                break
            case i:
                assert False, f"Instruction {i} not implemented yet"


class QueueReader:
    def __init__(self, id, queue):
        self.id = id
        self.queue = queue
        self.first = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.first:
            self.first = False
            return self.id
        if self.queue:
            return self.queue.pop(0)
        return -1


def part1(a):
    qs = [[] for _ in range(50)]
    comps = [(i, execute(a.copy(), QueueReader(i, qs[i]))) for i in range(50)]
    for i, c in cycle(comps):
        addr = next(c)
        if addr is None:
            continue
        x = next(c)
        y = next(c)
        if addr == 255:
            return y
        qs[addr].append(x)
        qs[addr].append(y)


def part2(a):
    qs = [[] for _ in range(50)]
    idles = [0 for _ in range(50)]
    comps = [(i, execute(a.copy(), QueueReader(i, qs[i]))) for i in range(50)]
    nat = (0, 0)
    prevnat = (0, 0)
    for i, c in cycle(comps):
        addr = next(c)
        if addr is None:
            idles[i] += 1
            if all(idle >= 10 for idle in idles) and not any(qs):
                if prevnat[1] == nat[1]:
                    return nat[1]
                prevnat = nat
                qs[0].append(nat[0])
                qs[0].append(nat[1])
            continue
        idles[i] = 0
        x = next(c)
        y = next(c)
        if addr == 255:
            nat = (x, y)
        else:
            qs[addr].append(x)
            qs[addr].append(y)


if __name__ == '__main__':
    data = get_data(day=23, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
