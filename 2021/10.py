from functools import reduce

from aocd import get_data

open_to_close = {'(': ')', '[': ']', '{': '}', '<': '>'}


def check_line(l):
    stack = []
    for c in l:
        if c in open_to_close:
            stack.append(open_to_close[c])
        else:
            if not stack.pop() == c:
                return True, c
    return False, ''.join(reversed(stack))


def part1(inp):
    return sum({')': 3, ']': 57, '}': 1197, '>': 25137}[closing]
               for invalid, closing in map(check_line, inp) if invalid)


def part2(inp):
    scores = sorted(reduce(lambda x, y: x * 5 + y, ({')': 1, ']': 2, '}': 3, '>': 4}[c] for c in closing))
                    for invalid, closing in map(check_line, inp) if not invalid)
    return scores[len(scores) // 2]


if __name__ == '__main__':
    data = get_data(day=10, year=2021)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
