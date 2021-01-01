from aocd import get_data


def reallocate(a):
    count = 0
    seen = dict()
    mem = a.copy()
    while True:
        if tuple(mem) in seen.keys():
            return count, seen[tuple(mem)]
        seen[tuple(mem)] = count
        count += 1

        index, n = max(enumerate(mem), key=lambda x: x[1])
        mem[index] = 0
        for i in range(index + 1, index + n + 1):
            mem[i % len(mem)] += 1


def part1(a):
    return reallocate(a)[0]


def part2(a):
    x, y = reallocate(a)
    return x - y


if __name__ == '__main__':
    data = get_data(day=6, year=2017)
    inp = list(map(int, data.split('\t')))
    print(part1(inp))
    print(part2(inp))
