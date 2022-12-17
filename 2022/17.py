from itertools import cycle
from operator import itemgetter

from aoc_utils import Vec
from aocd import data, submit, AocdError

rocks = [
    [Vec(0, 0), Vec(1, 0), Vec(2, 0), Vec(3, 0)],
    [Vec(1, 0), Vec(0, 1), Vec(1, 1), Vec(2, 1), Vec(1, 2)],
    [Vec(0, 0), Vec(1, 0), Vec(2, 0), Vec(2, 1), Vec(2, 2)],
    [Vec(0, 0), Vec(0, 1), Vec(0, 2), Vec(0, 3)],
    [Vec(0, 0), Vec(0, 1), Vec(1, 0), Vec(1, 1)]
]


def solve(inp, part1):
    mapp = {Vec(x, 0) for x in range(7)}
    inp_len = len(inp)
    dir_queue = cycle(inp)
    rock_count = 0
    jet_count = 0
    y_jump = 0
    known_states = {}

    for rock in cycle(rocks):
        ymax = max(map(itemgetter(1), mapp))
        rock_pos = Vec(2, ymax + 4)

        while True:
            dir = {"<": Vec(-1, 0), ">": Vec(1, 0)}[next(dir_queue)]
            jet_count += 1
            if all(0 <= (r + rock_pos + dir)[0] <= 6 and (r + rock_pos + dir) not in mapp for r in rock):
                rock_pos += dir

            if all((r + rock_pos + (0, -1)) not in mapp for r in rock):
                rock_pos += (0, -1)
            else:
                for r in rock:
                    mapp.add(r + rock_pos)
                break
            pass
        rock_count += 1
        if part1 and rock_count == 2022:
            return max(map(itemgetter(1), mapp))

        if not part1:
            if rock_count == 1000000000000:
                return max(map(itemgetter(1), mapp)) + y_jump
            ymax = max(map(itemgetter(1), mapp))
            top = frozenset((x, y) for x in range(7) for y in range(20) if (x, ymax - y) in mapp)

            state = (top, rock_count % 5, jet_count % inp_len)
            if state in known_states and y_jump == 0:
                old_rock_count, old_ymax = known_states[state]
                period = rock_count - old_rock_count
                repeat_count = ((1000000000000 - rock_count) // period)
                rock_count += period * repeat_count
                y_jump = (ymax - old_ymax) * repeat_count
            else:
                known_states[state] = (rock_count, ymax)


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
