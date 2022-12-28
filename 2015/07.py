import re


def evaluate(var, rules, cache):
    if var.isdigit():
        return int(var)
    if var not in cache:
        r = re.match(
            r"^("
            r"((?P<and1>\w+) AND (?P<and2>\w+))"
            r"|((?P<or1>\w+) OR (?P<or2>\w+))"
            r"|((?P<lshift1>\w+) LSHIFT (?P<lshift2>\d+))"
            r"|((?P<rshift1>\w+) RSHIFT (?P<rshift2>\d+))"
            r"|(NOT (?P<not>\w+))"
            r"|(?P<wire>\w+)"
            r")$",
            rules[var])
        if r.group('wire'):
            cache[var] = evaluate(r.group('wire'), rules, cache)
        elif r.group('and1'):
            cache[var] = evaluate(r.group('and1'), rules, cache) & evaluate(r.group('and2'), rules, cache)
        elif r.group('or1'):
            cache[var] = evaluate(r.group('or1'), rules, cache) | evaluate(r.group('or2'), rules, cache)
        elif r.group('not'):
            cache[var] = ~evaluate(r.group('not'), rules, cache)
        elif r.group('lshift1'):
            cache[var] = evaluate(r.group('lshift1'), rules, cache) << int(r.group('lshift2'))
        elif r.group('rshift1'):
            cache[var] = evaluate(r.group('rshift1'), rules, cache) >> int(r.group('rshift2'))
    return cache[var]


def solve(inp, part1):
    rules = {l.split('-> ')[1]: l.split(' ->')[0] for l in inp.splitlines()}
    if not part1:
        rules['b'] = str(evaluate('a', rules, {}))
    return evaluate('a', rules, {})


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
