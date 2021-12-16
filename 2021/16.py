import operator
from dataclasses import dataclass, field
from functools import reduce
from typing import Optional, List

from aocd import get_data


@dataclass
class Packet:
    version: int
    id: int
    immediate: Optional[int] = field(kw_only=True, default=None)
    subs: List['Packet'] = field(kw_only=True, default_factory=list)


def parse_int(s, pos, l):
    return int(s[pos:pos + l], 2), pos + l


def parse(s, pos):
    v, pos = parse_int(s, pos, 3)
    id, pos = parse_int(s, pos, 3)
    if id == 4:
        imm = 0
        flag = 1
        while flag:
            flag, pos = parse_int(s, pos, 1)
            tmp, pos = parse_int(s, pos, 4)
            imm = (imm << 4) + tmp
        return Packet(v, id, immediate=imm), pos
    else:
        typeid, pos = parse_int(s, pos, 1)
        length, pos = parse_int(s, pos, 11 if typeid else 15)
        content = []
        content_start = pos
        while (len(content) < length) if typeid else ((pos - content_start) < length):
            sub, pos = parse(s, pos)
            content.append(sub)
        return Packet(v, id, subs=content), pos


def version_sum(packet: Packet):
    return packet.version + sum(version_sum(p) for p in packet.subs)


def part1(inp):
    return version_sum(inp)


def evaluate(packet: Packet):
    match packet.id:
        case 0:
            return sum(evaluate(p) for p in packet.subs)
        case 1:
            return reduce(operator.mul, (evaluate(p) for p in packet.subs))
        case 2:
            return min(evaluate(p) for p in packet.subs)
        case 3:
            return max(evaluate(p) for p in packet.subs)
        case 4:
            return packet.immediate
        case 5:
            return 1 if evaluate(packet.subs[0]) > evaluate(packet.subs[1]) else 0
        case 6:
            return 1 if evaluate(packet.subs[0]) < evaluate(packet.subs[1]) else 0
        case 7:
            return 1 if evaluate(packet.subs[0]) == evaluate(packet.subs[1]) else 0
        case x:
            raise NotImplementedError(x)


def part2(inp):
    return evaluate(inp)


if __name__ == '__main__':
    data = get_data(day=16, year=2021)
    inp = parse(''.join(format(int(d, 16), '04b') for d in data), 0)[0]
    print(part1(inp))
    print(part2(inp))
