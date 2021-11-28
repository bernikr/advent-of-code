import math
from collections import defaultdict
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Reaction:
    input: list[tuple[int, str]]
    output: tuple[int, str]


def calculate_ore_cost_for_fuel(reacts: list[Reaction], fuel_amount: int) -> int:
    required = defaultdict(lambda: 0, {"FUEL": fuel_amount})
    surplus = defaultdict(lambda: 0)
    while list(required.keys()) != ["ORE"]:
        reqs, reqn = next((k, v) for k, v in required.items() if k != "ORE")
        react = next(r for r in reacts if r.output[1] == reqs)

        reactnum = math.ceil(reqn / react.output[0])
        surplus[reqs] += reactnum * react.output[0] - reqn
        del required[reqs]

        for n, e in react.input:
            if n*reactnum <= surplus[e]:
                surplus[e] -= n*reactnum
            else:
                required[e] += n*reactnum - surplus[e]
                del surplus[e]
        pass
    return required["ORE"]


def part1(a):
    return calculate_ore_cost_for_fuel(a, 1)


def part2(a):
    ore_inventory = 1000000000000
    lower, upper = 1, ore_inventory
    while upper-lower > 1:
        mid = (upper + lower) // 2
        cost = calculate_ore_cost_for_fuel(a, mid)
        if cost > ore_inventory:
            upper = mid
        else:
            lower = mid
    return lower


def parse_reaction(s: str) -> Reaction:
    inp, out = s.split(' => ')
    outn, outs = out.split(' ')
    inp = [(int(i.split(' ')[0]), i.split(' ')[1]) for i in inp.split(', ')]
    return Reaction(output=(int(outn), outs), input=inp)


if __name__ == '__main__':
    data = get_data(day=14, year=2019)
    inp = [parse_reaction(l) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
