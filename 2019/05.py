from aocd import get_data


def get_parameter(p, ip, n):
    flags = p[ip] // 100
    flag = (flags // 10**(n-1)) % 10
    match flag:
        case 0:
            return p[p[ip+n]]
        case 1:
            return p[ip+n]
        case i:
            assert False, f"Unknown Parameter Flag {i}"


def execute(p, inp):
    p = p.copy()
    ip = 0
    inp = inp.__iter__()
    output = []
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
                output.append(get_parameter(p, ip, 1))
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
                return output
            case i:
                assert False, f"Instruction {i} not implemented yet"


def part1(a):
    p = a.copy()
    return execute(p, [1])


def part2(a):
    p = a.copy()
    return execute(p, [5])


if __name__ == '__main__':
    data = get_data(day=5, year=2019)
    inp = list(map(int, data.split(',')))
    print(part1(inp))
    print(part2(inp))
