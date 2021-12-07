from aocd import get_data


def part1(inp):
    return min(sum(abs(x-c) for x in inp) for c in range(max(inp)))


def part2(inp):
    return min(sum(abs(x-c)*(abs(x-c)+1)//2 for x in inp) for c in range(max(inp)))


if __name__ == '__main__':
    data = get_data(day=7, year=2021)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
