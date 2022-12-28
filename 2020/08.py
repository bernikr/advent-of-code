def execute(program):
    pc, acc = 0, 0
    visited = set()
    while True:
        if pc == len(program):
            return 'terminated', acc
        if pc in visited:
            return 'loop', acc
        visited.add(pc)
        ins, imm = program[pc]
        if ins == 'acc':
            acc += imm
            pc += 1
        elif ins == 'jmp':
            pc += imm
        else:
            pc += 1


def part1(a):
    return execute(a)[1]


def part2(a):
    for i in range(0, len(a)):
        p = a.copy()
        if p[i][0] == 'nop':
            p[i] = ('jmp', p[i][1])
        elif p[i][0] == 'jmp':
            p[i] = ('nop', p[i][1])
        else:
            continue
        status, acc = execute(p)
        if status == 'terminated':
            return acc


def solve(inp, ispart1):
    inp = [(l.split(' ')[0], int(l.split(' ')[1])) for l in inp.splitlines()]
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
