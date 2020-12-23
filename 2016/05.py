import hashlib
import itertools

from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=5, year=2016)
    inp = data
    print(part1(inp))
    print(part2(inp))
