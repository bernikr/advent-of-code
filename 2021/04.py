from itertools import accumulate

from aocd import get_data


def check_win(board, nums):
    return any(all(x in nums for x in r) for r in board) or any(all(x in nums for x in c) for c in zip(*board))


def score(board, nums):
    return nums[-1] * sum(i for r in board for i in r if i not in nums)


def part1(inp):
    nums, boards = inp
    for i in range(len(nums)):
        called_nums = nums[:i + 1]
        for board in boards:
            if check_win(board, called_nums):
                return score(board, called_nums)


def part2(inp):
    nums, boards = inp
    won_boards = set()
    for i in range(len(nums)):
        called_nums = nums[:i + 1]
        for board in boards:
            if board not in won_boards and check_win(board, called_nums):
                won_boards.add(board)
                if len(won_boards) == len(boards):
                    return score(board, called_nums)


if __name__ == '__main__':
    data = get_data(day=4, year=2021)
    nums, *boards = data.split('\n\n')
    nums = list(map(int, nums.split(',')))
    boards = [tuple(tuple(int(x) for x in l.split(' ') if x != '') for l in b.splitlines()) for b in boards]
    inp = (nums, boards)
    print(part1(inp))
    print(part2(inp))
