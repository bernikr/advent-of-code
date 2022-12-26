from aocd import data, submit, AocdError

snafu_digits = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
snafu_digits_rev = {v: k for k, v in snafu_digits.items()}


def snafu_to_int(s):
    n = 0
    for c in s:
        n *= 5
        n += snafu_digits[c]
    return n


def int_to_snafu(n):
    if n == 0:
        return ""
    last_digit = n % 5
    if last_digit > 2:
        last_digit -= 5
    return int_to_snafu((n - last_digit) // 5) + snafu_digits_rev[last_digit]


def solve(inp):
    inp = inp.splitlines()
    return int_to_snafu(sum(map(snafu_to_int, inp)))


if __name__ == '__main__':
    try:
        submit(solve(data), part="a")
    except AocdError as e:
        print(e)
