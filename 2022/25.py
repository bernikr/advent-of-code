from aocd import data, submit, AocdError

snafu_digits = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
snafu_digits_rev = {v: k for k, v in snafu_digits.items()}


def snafu_to_int(s):
    return sum(5 ** i * snafu_digits[c] for i, c in enumerate(reversed(s)))


def int_to_snafu(n):
    return "" if n == 0 else int_to_snafu((n + 2) // 5) + snafu_digits_rev[(n + 2) % 5 - 2]


def solve(inp):
    inp = inp.splitlines()
    return int_to_snafu(sum(map(snafu_to_int, inp)))


if __name__ == '__main__':
    try:
        submit(solve(data), part="a")
    except AocdError as e:
        print(e)
