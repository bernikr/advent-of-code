rotate_right = lambda mapp: tuple(map(lambda x: ''.join(x), zip(*reversed(mapp))))
tilt = lambda mapp: tuple('#'.join("." * e.count(".") + "O" * e.count("O") for e in r.split("#")) for r in mapp)


def solve(inp, part1):
    mapp = inp.splitlines()
    mapp = rotate_right(mapp)  # we implement tilt to the right, so lets face north to the right
    if part1:
        mapp = tilt(mapp)
    else:
        seen = {}
        i = 1000000000
        shortcut = False
        while i > 0:
            i -= 1
            for _ in range(4):
                mapp = tilt(mapp)
                mapp = rotate_right(mapp)
            if not shortcut:
                if mapp in seen:
                    cycle_length = seen[mapp] - i
                    i = i % cycle_length
                    shortcut = True
                seen[mapp] = i
    return sum(sum(i if c == "O" else 0 for i, c in enumerate(r, 1)) for r in mapp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
