import re

from tqdm import tqdm


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

    def insert_next(self, data):
        next = self.next
        new = Node(data)
        self.next = new
        next.prev = new
        new.prev = self
        new.next = next
        return new

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


def solve(inp, part1):
    player_count, highest_num = map(int, re.findall(r"\d+", inp))
    if not part1:
        highest_num *= 100
    scores = [0] * player_count
    marble = Node(0)
    for i in tqdm(range(1, highest_num+1)):
        if i % 23 == 0:
            p = i % player_count
            scores[p] += i
            for _ in range(7):
                marble = marble.prev
            scores[p] += marble.data
            marble = marble.remove()
        else:
            marble = marble.next.insert_next(i)
    return max(scores)


if __name__ == '__main__':
    from aocd import data, submit, AocdError
    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
