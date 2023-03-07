from itertools import count


def step(state, rules):
    new_state = set()
    for i in range(min(state) - 2, max(state) + 3):
        cur = {j - i for j in state if -2 <= j - i <= 2}
        if any(cur == r for r in rules):
            new_state.add(i)
    return new_state


def solve(inp, part1):
    state, rules = inp.split("\n\n")
    state = {i for i, c in enumerate(state[15:]) if c == "#"}
    rules = [{i - 2 for i, c in enumerate(r[:5]) if c == "#"} for r in rules.splitlines() if r[-1] == "#"]
    if part1:
        for _ in range(20):
            state = step(state, rules)
        return sum(state)
    else:  # Part 2 requires the assumption that at some point every step will increase the sum by the same value
        last_steps = [0] * 10
        last_sum = 0
        for i in count(1):
            state = step(state, rules)
            s = sum(state)
            last_steps = [s - last_sum] + last_steps[:-1]
            last_sum = s
            if all(v == last_steps[0] for v in last_steps):
                return (50000000000-i)*last_steps[0] + s


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
