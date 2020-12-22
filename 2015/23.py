from aocd import get_data


def execute(program, a_start=0):
    pc = 0
    reg = {"a": a_start, "b": 0}
    while 0 <= pc < len(program):
        ins, *arg = program[pc]
        if ins == 'hlf':
            reg[arg[0]] //= 2
        elif ins == 'tpl':
            reg[arg[0]] *= 3
        elif ins == 'inc':
            reg[arg[0]] += 1
        elif ins == 'jmp':
            pc += int(arg[0])-1
        elif ins == 'jie':
            if reg[arg[0]] % 2 == 0:
                pc += int(arg[1])-1
        elif ins == 'jio':
            if reg[arg[0]] == 1:
                pc += int(arg[1])-1
        pc += 1
    return reg['b']


def part1(a):
    return execute(a)


def part2(a):
    return execute(a, 1)


if __name__ == '__main__':
    data = get_data(day=23, year=2015)
    inp = [tuple(l.replace(',', '').split(' ')) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
