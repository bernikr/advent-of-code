from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=2, year=2016)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
