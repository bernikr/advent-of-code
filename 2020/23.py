from collections import deque


# too slow for part 2
def play_queue(starting_arrangement, rounds):
    max_num = max(starting_arrangement)
    circle = deque(starting_arrangement)
    for _ in range(rounds):
        current = circle.popleft()
        pickup1 = circle.popleft()
        pickup2 = circle.popleft()
        pickup3 = circle.popleft()
        next_index = next(circle.index((current - i + max_num - 1) % max_num + 1)
                          for i in range(4) if (current - i + max_num - 1) % max_num + 1 in circle)
        circle.insert(next_index + 1, pickup1)
        circle.insert(next_index + 2, pickup2)
        circle.insert(next_index + 3, pickup3)
        circle.append(current)
    return list(circle)


def part1(a):
    res = ''.join(map(str, play_queue(a, 100)))
    return (res + res).split('1')[1]


class Cup:
    class CupIter:
        def __init__(self, cup):
            self.current = cup
            self.first = cup
            self.is_first = True

        def __next__(self):
            if not self.is_first and self.current == self.first:
                raise StopIteration
            self.is_first = False
            c = self.current
            self.current = self.current.next
            return c.n

    def __init__(self, n, next=None):
        self.n = n
        self.next = next

    def __repr__(self):
        return "<Cup: {}>".format(self.n)

    def __iter__(self):
        return Cup.CupIter(self)


# still very slow but manages part 2 in like a few minutes
def play_linked_list(starting_arrangement, rounds):
    max_num = max(starting_arrangement)
    # setup linked list and lookup list
    l = [None] * (len(starting_arrangement) + 1)
    current_cup = None
    prev_cup = None
    for i in starting_arrangement:
        l[i] = Cup(i)
        if current_cup is None:
            current_cup = l[i]
        if prev_cup is not None:
            prev_cup.next = l[i]
        prev_cup = l[i]
    prev_cup.next = current_cup
    for _ in range(rounds):
        first_pickup_node = current_cup.next
        pickup_nums = [first_pickup_node.n, first_pickup_node.next.n, first_pickup_node.next.next.n]
        next_num = next(j for j in
                        ((current_cup.n - i + max_num - 2) % max_num + 1 for i in range(4))
                        if j not in pickup_nums)
        next_node = l[next_num]
        # rearange nodes
        current_cup.next = first_pickup_node.next.next.next
        first_pickup_node.next.next.next = next_node.next
        next_node.next = first_pickup_node
        # advance to next node
        current_cup = current_cup.next
    return list(current_cup)


def part2(a):
    max_num = max(a)
    res = play_linked_list(a + [i for i in range(max_num + 1, 1000001)], 10000000)
    res = res + res
    i = res.index(1)
    return res[i + 1] * res[i + 2]


def solve(inp, ispart1):
    inp = list(map(int, inp))
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
