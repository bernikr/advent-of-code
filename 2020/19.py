from regex import regex


def create_regex(rules):
    return regex.compile(r"(?V1)(?(DEFINE){})^(?P>r0)$".format(''.join("(?<r{}>{})".format(k, ''.join(
        '|' if t == '|' else t[1] if t[0] == '"' else '(?P>r{})'.format(t) for t in v.split(' '))) for k, v in
                                                                       rules.items())))


def part1(a):
    rule = create_regex(a[0])
    return sum(1 if rule.match(l) is not None else 0 for l in a[1])


def part2(a):
    rules = a[0].copy()
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    rule = create_regex(rules)
    return sum(1 if rule.match(l) is not None else 0 for l in a[1])


def solve(inp, ispart1):
    inp = inp.split('\n\n')
    inp[0] = {int(l.split(':')[0]): l.split(': ')[1] for l in inp[0].splitlines()}
    inp[1] = inp[1].splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
