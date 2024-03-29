import itertools
import operator
import re
from functools import reduce

shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""
shop = {x.split(':')[0]: [tuple(map(int, re.findall(r" \d+", l))) for l in x.splitlines()[1:]] for x in
        shop.split('\n\n')}
shop['Armor'].append((0, 0, 0))
shop['Rings'].append((0, 0, 0))
shop['Rings'].append((0, 0, 0))


def fight(player_stats, boss_stats):
    p_hp, p_damage, p_armor = player_stats
    b_hp, b_damage, b_armor = boss_stats

    while True:
        b_hp -= max(1, p_damage - b_armor)
        if b_hp <= 0:
            return True
        p_hp -= max(1, b_damage - p_armor)
        if p_hp <= 0:
            return False


def solve(inp, part1):
    boss_stats = tuple(map(int, re.findall(r"\d+", inp)))
    equips = [(w, a, r1, r2) for w, a, r1, r2
              in itertools.product(shop['Weapons'], shop['Armor'], shop['Rings'], shop['Rings'])
              if r1 != r2 or r1 == (0, 0, 0)]

    if part1:
        return min(g for g, d, a in (reduce(lambda x, y: tuple(map(operator.add, x, y)), e) for e in equips)
                   if fight((100, d, a), boss_stats))
    else:
        return max(g for g, d, a in (reduce(lambda x, y: tuple(map(operator.add, x, y)), e) for e in equips)
                   if not fight((100, d, a), boss_stats))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
