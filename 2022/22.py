from aoc_utils import Vec
from aocd import data, submit, AocdError
from tqdm import tqdm


def move1(pos, dir, mapp):
    if (pos + dir) in mapp:
        return pos + dir
    step = max(max(p) for p in mapp)
    pos = pos - step * dir
    while pos not in mapp:
        pos += dir
    return pos


dirs = {
    "U": Vec(0, -1),
    "D": Vec(0, 1),
    "R": Vec(1, 0),
    "L": Vec(-1, 0),
}

# This edge mapping is hardcoded for my input and only works for nets with 50x50 squares that are shaped like this:
#     ##
#     #
#    ##
#    #
edges = [
    (Vec(51, 1), "U", "R", Vec(1, 151), "L", "D"),
    (Vec(101, 1), "U", "R", Vec(1, 200), "D", "R"),
    (Vec(150, 1), "R", "D", Vec(100, 150), "R", "U"),
    (Vec(150, 50), "D", "L", Vec(100, 100), "R", "U"),
    (Vec(51, 150), "D", "R", Vec(50, 151), "R", "D"),
    (Vec(1, 101), "L", "D", Vec(51, 50), "L", "U"),
    (Vec(1, 101), "U", "R", Vec(51, 51), "L", "D"),
]
edge_moves = {}
for a_begin, a_sides, a_dirs, b_begin, b_sides, b_dirs in edges:
    a_side, a_dir, b_side, b_dir = dirs[a_sides], dirs[a_dirs], dirs[b_sides], dirs[b_dirs]
    for i in range(50):
        a_pos = a_begin + a_dir * i
        b_pos = b_begin + b_dir * i
        edge_moves[(a_pos, a_side)] = (b_pos, -1 * b_side)
        edge_moves[(b_pos, b_side)] = (a_pos, -1 * a_side)


def move2(pos, dir, mapp):
    if (pos + dir) in mapp:
        return pos + dir, dir
    return edge_moves[(pos, dir)]


def solve(inp, part1):
    inp1, inp2 = inp.split('\n\n')
    mapp = {Vec(x, y): c for y, l in enumerate(inp1.splitlines(), 1) for x, c in enumerate(l, 1) if c != ' '}
    moves = list(map(lambda x: int(x) if x.isdigit() else x, inp2.replace("L", ",L,").replace("R", ",R,").split(",")))
    pos = Vec(1, 1)
    while pos not in mapp:
        pos += Vec(1, 0)
    dir = Vec(1, 0)
    for m in tqdm(moves):
        match m:
            case 'L':
                dir = Vec(dir[1], -dir[0])
            case 'R':
                dir = Vec(-dir[1], dir[0])
            case x:
                for _ in range(x):
                    if part1:
                        newpos = move1(pos, dir, mapp)
                        newdir = dir
                    else:
                        newpos, newdir = move2(pos, dir, mapp)
                    if mapp[newpos] == '#':
                        break
                    pos, dir = newpos, newdir
    return 1000 * pos[1] + 4 * pos[0] + {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[dir]


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
