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
    return oxy * co


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
