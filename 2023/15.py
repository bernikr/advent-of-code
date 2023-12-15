import re


def solve(inp, part1):
    h = lambda s: 0 if s == "" else ((h(s[:-1]) + ord(s[-1])) * 17) % 256

    ins = inp.split(',')
    if part1:
        return sum(h(s) for s in ins)
    else:
        boxes = [[] for _ in range(256)]
        values = {}
        for i in ins:
            label, op, value = re.match(r"([a-z]+)([=-])(\d*)", i).groups()
            if op == "=":
                values[label] = int(value)
                if label not in boxes[h(label)]:
                    boxes[h(label)].append(label)
            else:
                if label in boxes[h(label)]:
                    boxes[h(label)].remove(label)
        return sum(bn * sn * values[label] for bn, box in enumerate(boxes, 1) for sn, label in enumerate(box, 1))


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
