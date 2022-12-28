from aoc_utils import nth


def next_passwords(current_password):
    def increment_letter(letter):
        if letter == 'z':
            return 'a', True
        else:
            return chr(ord(letter) + 1), False

    p = current_password
    while True:
        new_password = ''
        increment = True
        for l in p[::-1]:
            new_letter = l
            if increment:
                new_letter, increment = increment_letter(l)
            new_password += new_letter
        p = new_password[::-1]
        yield p


def valid_passwords(previous_password):
    return (p for p in next_passwords(previous_password)
            if any(ord(p[i]) == ord(p[i + 1]) - 1 == ord(p[i + 2]) - 2 for i in range(len(p) - 2))
            and not any(l in p for l in 'iol')
            and any(p[i] == p[i + 1] and p[j] == p[j + 1] for i in range(len(p) - 1) for j in range(i + 2, len(p) - 1)))


def solve(inp, part1):
    return nth(valid_passwords(inp), 0 if part1 else 1)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
