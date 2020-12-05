def part1(a):
    return max(a)


def part2(a):
    return [i for i in range(min(a), max(a)) if i not in a and i+1 in a and i-1 in a][0]


if __name__ == '__main__':
    with open("5.input") as f:
        input = [int(''.join([{"F": "0", "B": "1", "L": "0", "R": "1"}[c] for c in l.strip()]), 2) for l in f.readlines()]
    print(part1(input))
    print(part2(input))
