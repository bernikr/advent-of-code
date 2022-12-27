from functools import reduce

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


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
