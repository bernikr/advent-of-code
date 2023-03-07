from dataclasses import dataclass
from itertools import count

from aoc_utils import Vec, dirs4
from tqdm import tqdm


@dataclass
class Unit:
    pos: Vec
    type: str
    hp: int = 200
    ap: int = 3

    @property
    def alive(self):
        return self.hp > 0


def run_battle(inp, elf_ap):
    mapp = {Vec(x, y) for y, l in enumerate(inp.splitlines()) for x, c in enumerate(l) if c != "#"}
    units = [Unit(Vec(x, y), c, ap=elf_ap if c == "E" else 3) for y, l in enumerate(inp.splitlines())
             for x, c in enumerate(l) if c in "GE"]
    empty = lambda: mapp - {u.pos for u in units if u.alive}
    read_sort = lambda v: (v[1], v[0])
    for i in count():
        for u in sorted(units, key=lambda u: read_sort(u.pos)):
            if not u.alive:
                continue
            targets = [t for t in units if t.type != u.type and t.alive]
            if not targets:
                return units, i * sum(u.hp for u in units if u.alive)
            range_candidates = {t.pos + d for t in targets for d in dirs4}
            if u.pos not in range_candidates:  # only move if not in range:
                rangee = range_candidates & empty()
                # find nearest range
                front = {u.pos: None}
                prevs = {}
                while True:
                    chosen_range = min((r for r in rangee if r in front), key=read_sort, default=None)
                    if chosen_range or not front:
                        break
                    prevs.update(front)
                    front = {c + d: c for c in front for d in dirs4 if c + d in empty() and c + d not in prevs}
                if not chosen_range:
                    continue
                # find next step
                front = {chosen_range: None}
                prevs = {}
                possible_steps = {u.pos + d for d in dirs4} & empty()
                while True:
                    next_step = min((s for s in possible_steps if s in front), key=read_sort, default=None)
                    if next_step:
                        break
                    prevs.update(front)
                    front = {c + d: c for c in front for d in dirs4 if c + d in empty() and c + d not in prevs}
                u.pos = next_step
            # Combat
            if u.pos in range_candidates:
                t = min((t for t in targets if t.pos in {u.pos + d for d in dirs4}),
                        key=lambda t: (t.hp, read_sort(t.pos)))
                t.hp -= u.ap


def solve(inp, part1):
    if part1:
        return run_battle(inp, 3)[1]
    else:
        for ap in tqdm(count(4)):
            units, outcome = run_battle(inp, ap)
            if all(u.alive for u in units if u.type == "E"):
                return outcome


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
