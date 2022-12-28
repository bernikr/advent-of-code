from itertools import permutations, chain


def get_parameter(p, ip, n):
    flags = p[ip] // 100
    flag = (flags // 10 ** (n - 1)) % 10
    match flag:
        case 0:
            return p[p[ip + n]]
        case 1:
            return p[ip + n]
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def execute(p, inp):
    p = p.copy()
    ip = 0
    while True:
        match p[ip] % 100:
            case 1:
                p[p[ip + 3]] = get_parameter(p, ip, 1) + get_parameter(p, ip, 2)
                ip += 4
            case 2:
                p[p[ip + 3]] = get_parameter(p, ip, 1) * get_parameter(p, ip, 2)
                ip += 4
            case 3:
                p[p[ip + 1]] = next(inp)
                ip += 2
            case 4:
                yield get_parameter(p, ip, 1)
                ip += 2
            case 5:
                if get_parameter(p, ip, 1) != 0:
                    ip = get_parameter(p, ip, 2)
                else:
                    ip += 3
            case 6:
                if get_parameter(p, ip, 1) == 0:
                    ip = get_parameter(p, ip, 2)
                else:
                    ip += 3
            case 7:
                p[p[ip + 3]] = 1 if get_parameter(p, ip, 1) < get_parameter(p, ip, 2) else 0
                ip += 4
            case 8:
                p[p[ip + 3]] = 1 if get_parameter(p, ip, 1) == get_parameter(p, ip, 2) else 0
                ip += 4
            case 99:
                break
            case i:
                assert False, f"Instruction {i} not implemented yet"


def part1(a):
    res = []
    for perm in permutations([0, 1, 2, 3, 4]):
        inp = 0
        for val in perm:
            p = a.copy()
            inp = next(execute(p, [val, inp].__iter__()))
        res.append(inp)
    return max(res)


def part2(a):
    res = []
    for perm in permutations([5, 6, 7, 8, 9]):
        it = [0]
        inp = it
        for val in perm:
            p = a.copy()
            inp = execute(p, chain([val], inp))
        for i in inp:
            it.append(i)
        res.append(i)

    return max(res)


def solve(inp, ispart1):
    inp = list(map(int, inp.split(',')))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
