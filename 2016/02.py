def get_code(keypad, start, moves):
    move_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    x, y = start
    code = ''
    for l in moves:
        for c in l:
            dx, dy = move_map[c]
            if 0 <= x + dx < len(keypad) and 0 <= y + dy < len(keypad[0]) and keypad[x + dx][y + dy] != ' ':
                x += dx
                y += dy
        code += str(keypad[x][y])
    return code


def part1(a):
    return get_code(['123', '456', '789'], (1, 1), a)


def part2(a):
    return get_code(['  1  ', ' 234 ', '56789', ' ABC ', '  D  '], (2, 0), a)


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
