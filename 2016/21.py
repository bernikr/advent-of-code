from aocd import get_data

def rotate_based_on_letter(s, x):
    res = s.copy()
    i = res.index(x)
    rots = 1 + i + (1 if i >= 4 else 0)
    for _ in range(rots):
        res = [res[-1]] + res[:-1]
    return res


def perform_op(s, op):
    res = list(s)
    match op.split(' '):
        case ['swap', 'position', x, 'with', 'position', y]:
            x, y = int(x), int(y)
            res[x] = s[y]
            res[y] = s[x]
        case ['swap', 'letter', x, 'with', 'letter', y]:
            res = [x if l == y else y if l == x else l for l in res]
        case ['reverse', 'positions', x, 'through', y]:
            x, y = int(x), int(y)
            res[x:y + 1] = reversed(res[x:y + 1])
        case ['rotate', 'left', x, 'steps' | 'step']:
            for _ in range(int(x)):
                res = res[1:] + [res[0]]
        case ['rotate', 'right', x, 'steps' | 'step']:
            for _ in range(int(x)):
                res = [res[-1]] + res[:-1]
        case ['move', 'position', x, 'to', 'position', y]:
            x, y = int(x), int(y)
            e = res[x]
            del res[x]
            res.insert(y, e)
        case ['rotate', 'based', 'on', 'position', 'of', 'letter', x]:
            res = rotate_based_on_letter(res, x)
        case x:
            raise NotImplementedError(x)
    return ''.join(res)


def reverse_op(s, op):
    res = list(s)
    match op.split(' '):
        case ['swap', 'position', x, 'with', 'position', y]:
            x, y = int(x), int(y)
            res[x] = s[y]
            res[y] = s[x]
        case ['swap', 'letter', x, 'with', 'letter', y]:
            res = [x if l == y else y if l == x else l for l in res]
        case ['reverse', 'positions', x, 'through', y]:
            x, y = int(x), int(y)
            res[x:y + 1] = reversed(res[x:y + 1])
        case ['rotate', 'right', x, 'steps' | 'step']:
            for _ in range(int(x)):
                res = res[1:] + [res[0]]
        case ['rotate', 'left', x, 'steps' | 'step']:
            for _ in range(int(x)):
                res = [res[-1]] + res[:-1]
        case ['move', 'position', x, 'to', 'position', y]:
            x, y = int(x), int(y)
            e = res[y]
            del res[y]
            res.insert(x, e)
        case ['rotate', 'based', 'on', 'position', 'of', 'letter', x]:
            tmp = res.copy()
            for _ in range(len(s)):
                tmp = tmp[1:] + [tmp[0]]
                if rotate_based_on_letter(tmp, x) == res:
                    res = tmp
                    break

        case x:
            raise NotImplementedError(x)
    return ''.join(res)


def part1(inp):
    s = 'abcdefgh'
    for op in inp:
        s = perform_op(s, op)
    return s


def part2(inp):
    s = 'fbgdceah'
    for op in reversed(inp):
        s = reverse_op(s, op)
    return s


if __name__ == '__main__':
    data = get_data(day=21, year=2016)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
