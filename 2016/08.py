import re

from aocd import get_data


class Display:
    def __init__(self, rows, columns):
        self.pixels = [['.' for _ in range(columns)] for _ in range(rows)]

    def __iter__(self):
        return self.pixels.__iter__()

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.pixels)

    def rect(self, x, y):
        for i in range(x):
            for j in range(y):
                self.pixels[j][i] = '#'

    def rotate_row(self, row_num, n):
        for _ in range(n):
            last = self.pixels[row_num][-1]
            for i in range(len(self.pixels[row_num])-1, 0, -1):
                self.pixels[row_num][i] = self.pixels[row_num][i-1]
            self.pixels[row_num][0] = last

    def rotate_column(self, col_num, n):
        temp = list(map(list, zip(*self.pixels)))
        for _ in range(n):
            last = temp[col_num][-1]
            for i in range(len(temp[col_num])-1, 0, -1):
                temp[col_num][i] = temp[col_num][i-1]
            temp[col_num][0] = last
        self.pixels = list(map(list, zip(*temp)))

def run_instructions(display, instructions):
    for l in instructions:
        if l[0] is not None:
            display.rect(l[0], l[1])
        elif l[2] == 'y':
            display.rotate_row(l[3], l[4])
        else:
            display.rotate_column(l[3], l[4])


def part1(a):
    d = Display(6, 50)
    run_instructions(d, a)
    return str(d).count('#')


def part2(a):
    d = Display(6, 50)
    run_instructions(d, a)
    return str(d)


if __name__ == '__main__':
    data = get_data(day=8, year=2016)
    inp = [tuple(int(x) if x is not None and x.isnumeric() else x
                 for x in re.match(r"(?:rect (\d+)x(\d+)|rotate \w+ ([xy])=(\d+) by (\d+))", l).groups())
           for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
