def reallocate(a):
    count = 0
    seen = dict()
    mem = a.copy()
    while True:
        if tuple(mem) in seen.keys():
            return count, seen[tuple(mem)]
        seen[tuple(mem)] = count
        count += 1

        index, n = max(enumerate(mem), key=lambda x: x[1])
        mem[index] = 0
        for i in range(index + 1, index + n + 1):
            mem[i % len(mem)] += 1


def solve(inp, ispart1):
    inp = list(map(int, inp.split('\t')))
    x, y = reallocate(inp)
    return x if ispart1 else x - y


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
