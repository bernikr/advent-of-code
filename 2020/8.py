from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=8, year=2020)
    input = [(l.split(' ')[0], int(l.split(' ')[1])) for l in data.splitlines()]
    print(part1(input))
    print(part2(input))
