def look_and_say(s):
    out = ''
    char = s[0]
    count = 1
    for c in s[1:]:
        if c != char:
            out += str(count) + char
            char = c
            count = 1
        else:
            count += 1
    out += str(count) + char
    return out


def solve(inp, part1):
    for _ in range(40 if part1 else 50):
        inp = look_and_say(inp)
    return len(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
