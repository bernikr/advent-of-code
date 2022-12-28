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
            pc += int(arg[0]) - 1
        elif ins == 'jie':
            if reg[arg[0]] % 2 == 0:
                pc += int(arg[1]) - 1
        elif ins == 'jio':
            if reg[arg[0]] == 1:
                pc += int(arg[1]) - 1
        pc += 1
    return reg['b']


def solve(inp, part1):
    inp = [tuple(l.replace(',', '').split(' ')) for l in inp.splitlines()]
    return execute(inp, 0 if part1 else 1)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
