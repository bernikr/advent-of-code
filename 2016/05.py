import hashlib
import itertools


def part1(a):
    return ''.join(itertools.islice(
        (h[5] for h in (hashlib.md5((a + str(i)).encode('utf-8')).hexdigest() for i in itertools.count())
         if h.startswith('0' * 5)), 8))


def part2(a):
    code = [' ' for _ in range(8)]
    hash_seq = ((h[5], h[6]) for h in (hashlib.md5((a + str(i)).encode('utf-8')).hexdigest() for i in itertools.count())
                if h.startswith('0' * 5))
    while ' ' in code:
        pos, c = next(hash_seq)
        if pos in '01234567' and code[int(pos)] == ' ':
            code[int(pos)] = c
    return ''.join(code)


def solve(inp, ispart1):
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
