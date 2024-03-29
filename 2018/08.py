class Node:
    def __init__(self):
        self.children = []
        self.metadata = []


def parse(inp):
    num_children = inp[0]
    num_metadata = inp[1]
    node = Node()
    rest_inp = inp[2:]
    for i in range(num_children):
        child, rest_inp = parse(rest_inp)
        node.children.append(child)
    node.metadata = rest_inp[:num_metadata]
    return node, rest_inp[num_metadata:]


def metadata_sum(node):
    return sum(node.metadata) + sum(metadata_sum(n) for n in node.children)


def value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        return sum(value(node.children[i - 1]) for i in node.metadata if 1 <= i <= len(node.children))


def solve(inp, ispart1):
    inp = parse(list(map(int, inp.split(' '))))[0]
    return metadata_sum(inp) if ispart1 else value(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
