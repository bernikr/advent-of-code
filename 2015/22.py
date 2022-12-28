import re
from collections import deque


class Spell:
    def __init__(self, name, cost, duration, damage=0, heal=0, armor=0, mana=0):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.mana = mana

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()

    def __repr__(self):
        return self.name

    def copy(self):
        return Spell(**self.__dict__)


spells = [
    Spell("Magic Missile", 53, 1, damage=4),
    Spell("Drain", 73, 1, damage=2, heal=2),
    Spell("Shield", 113, 6, armor=7),
    Spell("Poison", 173, 6, damage=3),
    Spell("Recharge", 229, 5, mana=101)
]


def fight(boss_stats, actions, hard_mode=False):
    p_hp, p_mana = 50, 500
    b_hp, b_damage = boss_stats
    current_effects = set()
    total_cost = 0
    actions = deque(actions)

    for i in range(2 * len(actions) + 2):
        p_armor = 0

        if hard_mode and i % 2 == 0:
            p_hp -= 1
            if p_hp == 0:
                return 'b', total_cost

        # apply effects and decrease their duration
        for e in list(current_effects):
            b_hp -= e.damage
            p_hp += e.heal
            p_armor += e.armor
            p_mana += e.mana
            e.duration -= 1
            if e.duration == 0:
                current_effects.remove(e)

        # check if boss died
        if b_hp <= 0:
            return 'p', total_cost

        if i % 2 == 0:
            if len(actions) == 0:
                return None, total_cost
            spell = actions.popleft()
            if spell in current_effects or spell.cost >= p_mana:
                return 'b', total_cost
            current_effects.add(spell.copy())
            total_cost += spell.cost
            p_mana -= spell.cost
        else:
            p_hp -= max(1, b_damage - p_armor)
            if p_hp <= 0:
                return 'b', total_cost


def find_least_mana_win(boss_stats, hard_mode=False):
    open_branches = deque([[]])
    min_mana = 99999999999
    while len(open_branches) > 0:
        actions = open_branches.popleft()
        winner, mana = fight(boss_stats, actions, hard_mode)
        if winner == 'p':
            min_mana = min(mana, min_mana)
        elif winner is None:
            if mana < min_mana:
                for s in spells:
                    open_branches.append(actions + [s])
    return min_mana


def solve(inp, part1):
    inp = tuple(map(int, re.findall(r"\d+", inp)))
    return find_least_mana_win(inp, hard_mode=not part1)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
