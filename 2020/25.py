import itertools

from aocd import get_data


def get_loop_size(subject_num, goal):
    n = 1
    for i in itertools.count():
        if n == goal:
            return i
        n = (n * subject_num) % 20201227


def transform(subject_num, loop_size):
    n = 1
    for i in range(loop_size):
        n = (n * subject_num) % 20201227
    return n


def part1(a):
    l0 = get_loop_size(7, a[0])
    return transform(a[1], l0)


if __name__ == '__main__':
    data = get_data(day=25, year=2020)
    inp = tuple(map(int, data.splitlines()))
    print(part1(inp))
