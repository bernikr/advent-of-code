from itertools import count

from tqdm import tqdm


def solve(inp, part1):
    inpn = int(inp)
    inpl = len(inp)
    board = "37"
    elves = [0, 1]
    for _ in tqdm(count()):
        board += str(int(board[elves[0]]) + int(board[elves[1]]))
        elves = [(e + 1 + int(board[e])) % len(board) for e in elves]
        if part1 and len(board) > inpn + 10:
            return board[inpn: inpn + 10]
        if not part1 and (inp == board[-inpl:] or inp == board[-inpl - 1:-1]):
            return board.find(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
