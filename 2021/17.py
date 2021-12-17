import re

from aoc_utils import Vec, sign, Rect
from aocd import get_data


def step(pos, vel):
    pos += vel
    vel += (-sign(vel[0]), -1)
    return pos, vel


def check_y_hit(vel, target):
    pos = Vec(0, 0)
    while True:
        pos, vel = step(pos, vel)
        if target.lower[1] <= pos[1] <= target.upper[1]:
            return True
        elif pos[1] < target.lower[1] and vel[1] < 0:
            return False


def check_x_hit(vel, target):
    pos = Vec(0, 0)
    while True:
        pos, vel = step(pos, vel)
        if target.lower[0] <= pos[0] <= target.upper[0]:
            return True
        elif vel[0] == 0:
            return False


def check_hit(vel, target):
    pos = Vec(0, 0)
    while True:
        pos, vel = step(pos, vel)
        if pos in target:
            return True
        elif pos[1] < target.lower[1] and vel[1] < 0:
            return False


def part1(inp):
    y_vel = 0
    for i in range(min(0, inp.lower[1] - 1), max(abs(y) for _, y in [inp.lower, inp.upper]) + 1):
        if check_y_hit(Vec(0, i), inp):
            y_vel = i
    max_y = 0
    pos = Vec(0, 0)
    vel = Vec(0, y_vel)
    while True:
        pos, vel = step(pos, vel)
        if pos[1] < max_y:
            return max_y
        max_y = pos[1]


def part2(inp):
    y_candidates = []
    for i in range(min(0, inp.lower[1] - 1), max(abs(y) for _, y in [inp.lower, inp.upper]) + 1):
        if check_y_hit(Vec(0, i), inp):
            y_candidates.append(i)
    x_candidates = []
    for i in range(min(0, inp.lower[0] - 1), max(0, inp.upper[0] + 1)):
        if check_x_hit(Vec(i, 0), inp):
            x_candidates.append(i)
    return sum(check_hit(Vec(x, y), inp) for x in x_candidates for y in y_candidates)


if __name__ == '__main__':
    data = get_data(day=17, year=2021)
    inp = tuple(map(int, re.match(r'^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$', data).groups()))
    inp = Rect(Vec(inp[0], inp[2]), Vec(inp[1], inp[3]))
    print(part1(inp))
    print(part2(inp))
