from aocd import get_data


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


def part1(a):
    return next(valid_passwords(a))


def part2(a):
    return next(p for i, p in enumerate(valid_passwords(a)) if i == 1)


if __name__ == '__main__':
    data = get_data(day=11, year=2015)
    inp = data
    print(part1(inp))
    print(part2(inp))
