def solve(inp, part1):
    p = list(map(int, inp.splitlines()))
    ip = 0
    i = 0
    while True:
        if not 0 <= ip < len(p):
            return i
        prev_ip = ip
        ip = ip + p[ip]
        p[prev_ip] += 1 if part1 or p[prev_ip] < 3 else -1
        i += 1


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
