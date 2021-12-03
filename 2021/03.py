from aocd import get_data


def part1(inp):
    return int(''.join('1' if sum(int(d) for d in digits) / len(digits) > 0.5 else '0' for digits in zip(*inp)), 2) * \
           int(''.join('1' if sum(int(d) for d in digits) / len(digits) < 0.5 else '0' for digits in zip(*inp)), 2)


def part2(inp):
    li = inp.copy()
    d = 0
    while len(li) > 1:
        most_common = '1' if sum(int(n[d]) for n in li) / len(li) >= 0.5 else '0'
        li = [n for n in li if n[d] == most_common]
        d += 1
    oxy = int(li[0], 2)
    li = inp.copy()
    d = 0
    while len(li) > 1:
        least_common = '1' if sum(int(n[d]) for n in li) / len(li) < 0.5 else '0'
        li = [n for n in li if n[d] == least_common]
        d += 1
    co = int(li[0], 2)
    return oxy*co


if __name__ == '__main__':
    data = get_data(day=3, year=2021)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
