import math
import re
from itertools import product

from tqdm import tqdm

from aoc_utils import Box


# returns a list of open boxes completely surrounding the given box, but not overlapping
def invert_box(box):
    dim = len(box.lower)
    for pos in product((-1, 0, 1), repeat=dim):
        if all(x == 0 for x in pos):
            continue
        lower, upper = [None] * dim, [None] * dim
        for d in range(dim):
            if pos[d] == -1:
                lower[d] = -math.inf
                upper[d] = box.lower[d] - 1
            elif pos[d] == 0:
                lower[d] = box.lower[d]
                upper[d] = box.upper[d]
            elif pos[d] == 1:
                lower[d] = box.upper[d] + 1
                upper[d] = math.inf
        yield Box(lower, upper)


class BoxSet:
    def __init__(self, *boxes):
        self.boxes = []
        add_queue = []
        for b in boxes:
            if isinstance(b, Box):
                add_queue.append(b)
            elif isinstance(b, BoxSet):
                add_queue += b.boxes
            else:
                raise TypeError("BoxSet can only be initialized with Box or BoxSet elements")
        while add_queue:
            nb = add_queue.pop()
            if nb.is_empty():
                continue
            if all(not nb.overlaps(b) for b in self.boxes):
                self.boxes.append(nb)
            else:
                other = next(b for b in self.boxes if nb.overlaps(b))
                overlap = other & nb
                for inversion_part in invert_box(overlap):
                    new_segment = inversion_part & nb
                    if not new_segment.overlaps(other):
                        add_queue.append(new_segment)

    def __or__(self, other):
        if isinstance(other, Box) or isinstance(other, BoxSet):
            return BoxSet(self, other)
        else:
            raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, Box):
            return BoxSet(self, other) & BoxSet(*invert_box(other))
        else:
            raise NotImplementedError()

    def __and__(self, other):
        if isinstance(other, Box):
            return BoxSet(*(b & other for b in self.boxes))
        if isinstance(other, BoxSet):
            return BoxSet(*(other & b for b in self.boxes))
        else:
            raise NotImplementedError()

    def size(self):
        return sum(b.size() for b in self.boxes)


def solve(inp, part1):
    inp = [(action, Box((x1, y1, z1), (x2, y2, z2))) for action, x1, x2, y1, y2, z1, z2 in
           (map(lambda x: x if x in ["on", "off"] else int(x),
                re.match(r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", l).groups())
            for l in inp.splitlines())]
    lights = BoxSet()
    for action, box in tqdm(inp):
        if action == "on":
            lights |= box
        else:
            lights -= box
    if part1:
        return (lights & Box((-50,) * 3, (50,) * 3, )).size()
    else:
        return lights.size()


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    print(solve("""on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682""", True))

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
