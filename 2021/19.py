from collections import Counter
from itertools import product
from operator import itemgetter

from aoc_utils import Vec, Matrix


# Adapted from https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
# Returns all 24 rotations of a given point around the origin
def rotations(v):
    roll = lambda x: Vec(x[0], x[2], -x[1])
    turn = lambda x: Vec(-x[1], x[0], x[2])
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield v  # Yield R
            for i in range(3):  # Yield TTT
                v = turn(v)
                yield v
        v = roll(turn(roll(v)))  # Do RTR


rotation_matrices = [Matrix(*r) for r in zip(*(rotations(e) for e in [Vec(1, 0, 0), Vec(0, 1, 0), Vec(0, 0, 1)]))]


def get_match_anchor_candidates(reference, scanner):
    ref_fps = {a: Counter((a - b).manhatten() for b in reference) for a in reference}
    scan_fps = {a: Counter((a - b).manhatten() for b in scanner) for a in list(scanner)[11:]}

    for ref_anchor, ref_anchor_fp in ref_fps.items():
        for anchor, anchor_fp in scan_fps.items():
            if (anchor_fp & ref_anchor_fp).total() >= 12:
                yield ref_anchor, anchor


def find_match(reference, scanner):
    for ref_anchor, anchor in get_match_anchor_candidates(reference, scanner):
        for rot in rotation_matrices:
            trans = ref_anchor - rot * anchor
            overlap = sum(1 if rot * b + trans in reference else 0 for b in scanner)
            if overlap >= 12:
                return rot, trans
    return None


def solve(inp, part1):
    scanners = [{Vec(*map(int, l.split(','))) for l in s.splitlines()[1:]} for s in inp.split("\n\n")]
    mapp = scanners[0]
    # initialize the first scanner as reference with no translation or rotation
    mapped_scanners = {0: (Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)), Vec(0, 0, 0))}
    unmapped_scanners = list(range(1, len(scanners)))
    compared = set()
    while unmapped_scanners:
        for unmapped, mapped in product(unmapped_scanners, reversed(mapped_scanners.keys())):
            if (unmapped, mapped) not in compared:
                compared.add((unmapped, mapped))
                compared.add((mapped, unmapped))
                res = find_match(scanners[mapped], scanners[unmapped])
                if res:
                    relative_rot, relative_trans = res
                    reference_rot, reference_trans = mapped_scanners[mapped]
                    rot = reference_rot * relative_rot
                    trans = reference_rot * relative_trans + reference_trans
                    mapped_scanners[unmapped] = (rot, trans)
                    unmapped_scanners.remove(unmapped)
                    mapp |= {rot * b + trans for b in scanners[unmapped]}
                    break

    if part1:
        return len(mapp)
    else:
        return max((a - b).manhatten() for a, b in product(map(itemgetter(1), mapped_scanners.values()), repeat=2))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
