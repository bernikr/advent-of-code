from collections import Counter
from collections.abc import Iterable


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    state = Counter(int(x) for x in inp.split())
    for i in range(75):
        new_state = Counter()
        for num, count in state.items():
            if num == 0:
                new_state[1] += count
            elif (l := len(str(num))) % 2 == 0:
                new_state[int(str(num)[:l // 2])] += count
                new_state[int(str(num)[l // 2:])] += count
            else:
                new_state[num * 2024] += count
        state = new_state
        if i == 24:
            yield 1, sum(state.values())
    yield 2, sum(state.values())


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
