from aocd import data, submit, AocdError
from tqdm import tqdm


def solve(inp, part1):
    inp = map(int, inp.splitlines())
    if not part1:
        inp = map(lambda x: x * 811589153, inp)
    inp = list(enumerate(inp))
    length = len(inp)
    for item in tqdm(inp.copy() * (1 if part1 else 10)):
        pos = inp.index(item)
        inp.remove(item)
        pos = (pos + item[1]) % (length - 1)
        inp.insert(pos, item)
    zero = inp.index(next(i for i in inp if i[1] == 0))
    return inp[(zero + 1000) % length][1] + inp[(zero + 2000) % length][1] + inp[(zero + 3000) % length][1]


if __name__ == '__main__':
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
