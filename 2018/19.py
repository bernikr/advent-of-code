def solve(inp, part1):
    program = [tuple(map(lambda x: int(x) if x.isnumeric() else x, l.split(" "))) for l in inp.splitlines()]
    assert program[0][0] == "#ip"
    ipp = program[0][1]
    program = program[1:]
    r = [0] * 6
    if not part1:
        r[0] = 1
    while 0 <= r[ipp] < len(program):
        match program[r[ipp]]:
            case ("addr", a, b, c):
                r[c] = r[a] + r[b]
            case ("addi", a, b, c):
                r[c] = r[a] + b
            case ("mulr", a, b, c):
                r[c] = r[a] * r[b]
            case ("muli", a, b, c):
                r[c] = r[a] * b
            case ("banr", a, b, c):
                r[c] = r[a] & r[b]
            case ("bani", a, b, c):
                r[c] = r[a] & b
            case ("borr", a, b, c):
                r[c] = r[a] | r[b]
            case ("bori", a, b, c):
                r[c] = r[a] | b
            case ("setr", a, b, c):
                r[c] = r[a]
            case ("seti", a, b, c):
                r[c] = a
            case ("gtir", a, b, c):
                r[c] = 1 if a > r[b] else 0
            case ("gtri", a, b, c):
                r[c] = 1 if r[a] > b else 0
            case ("gtrr", a, b, c):
                r[c] = 1 if r[a] > r[b] else 0
            case ("eqir", a, b, c):
                r[c] = 1 if a == r[b] else 0
            case ("eqri", a, b, c):
                r[c] = 1 if r[a] == b else 0
            case ("eqrr", a, b, c):
                r[c] = 1 if r[a] == r[b] else 0
            case x:
                raise NotImplementedError(x)
        r[ipp] += 1
    return r[0]


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
