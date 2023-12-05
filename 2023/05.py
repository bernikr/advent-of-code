import re
from dataclasses import dataclass
from operator import attrgetter

from more_itertools import batched


def single_mapper(x, mappings):
    for dest_start, source_start, length in mappings:
        if source_start <= x < source_start + length:
            return x - source_start + dest_start
    return x


def complete_mapper(x, mappingss):
    for mapping in mappingss:
        x = single_mapper(x, mapping)
    return x


@dataclass
class Range:
    start: int
    length: int

    @property
    def end(self):
        return self.start + self.length - 1

    def __and__(self, other):
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        if end >= start:
            return Range(start, end - start + 1)
        else:
            return Range(0, 0)

    def split_by_range(self, other):
        if self & other == Range(0, 0):
            return [self]
        start1 = self.start
        end1 = other.start - 1
        start2 = other.end + 1
        end2 = self.end
        range1 = Range(start1, end1 - start1 + 1) if end1 >= start1 else Range(0, 0)
        range2 = Range(start2, end2 - start2 + 1) if end2 >= start2 else Range(0, 0)
        return simplify_ranges([range1, range2])


def simplify_ranges(ranges):
    ranges = [r for r in ranges if r.length > 0]
    # TODO: possible optimization: join overlapping and consecutive ranges
    return ranges


def map_range(r, mappings):
    res = []
    for dest_start, source_start, length in mappings:
        source_range = Range(source_start, length)
        overlap = r & source_range
        overlap.start += dest_start - source_start
        res.append(overlap)
    remaining = [r]
    for _, source_start, length in mappings:
        new_remaining = []
        for rrange in remaining:
            new_remaining.extend(rrange.split_by_range(Range(source_start, length)))
        remaining = new_remaining
    res.extend(remaining)
    res = simplify_ranges(res)
    return res


def solve(inp, part1):
    seeds, *inp = inp.split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", seeds)))
    mapss = [[tuple(map(int, res)) for res in re.findall(r"(\d+) (\d+) (\d+)", m)] for m in inp]
    if part1:
        return min([complete_mapper(x, mapss) for x in seeds])
    else:
        ranges = [Range(a, b) for a, b in batched(seeds, 2)]
        for maps in mapss:
            new_ranges = []
            for r in ranges:
                new_ranges.extend(map_range(r, maps))
            ranges = simplify_ranges(new_ranges)
        return min(map(attrgetter('start'), ranges))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
