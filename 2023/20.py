import math
from collections import deque
from functools import reduce
from itertools import count

HIGH, LOW = True, False
ON, OFF = True, False


def run(node_type, node_connections, flip_state, conj_state, inital_pulse):
    msg_queue = deque()
    msg_queue.append(inital_pulse)
    while msg_queue:
        from_module, to_module, pulse = msg_queue.popleft()
        yield from_module, to_module, pulse
        if to_module not in node_type:  # node has no outgoing connections
            continue
        if node_type[to_module] == "b":
            for c in node_connections[to_module]:
                msg_queue.append((to_module, c, pulse))
        elif node_type[to_module] == "%":
            if pulse == LOW:
                flip_state[to_module] = not flip_state[to_module]
                out_pulse = HIGH if flip_state[to_module] == ON else LOW
                for c in node_connections[to_module]:
                    msg_queue.append((to_module, c, out_pulse))
        elif node_type[to_module] == "&":
            conj_state[to_module][from_module] = pulse
            out_pulse = LOW if all(x == HIGH for x in conj_state[to_module].values()) else HIGH
            for c in node_connections[to_module]:
                msg_queue.append((to_module, c, out_pulse))
        else:
            assert False


def solve_part1(node_type, node_connections):
    flip_state = {name: OFF for name, t in node_type.items() if t == "%"}
    conj_state = {name: {n: LOW for n, conns in node_connections.items() if name in conns}
                  for name, t in node_type.items() if t == "&"}
    pulses = [0, 0]
    for _ in range(1000):
        for _, _, p in run(node_type, node_connections, flip_state, conj_state, ("button", "roadcaster", LOW)):
            pulses[p] += 1

    return pulses[0] * pulses[1]


def solve_part2(node_type, node_connections):
    # assume a connection graph that consists of x subgraphs connected at the broadcaster and one & node before rx
    combiner_node = [n for n, conns in node_connections.items() if "rx" in conns]
    assert len(combiner_node) == 1 and node_type[combiner_node[0]] == "&"
    combiner_node = combiner_node[0]

    flip_state = {name: OFF for name, t in node_type.items() if t == "%"}
    conj_state = {name: {n: LOW for n, conns in node_connections.items() if name in conns}
                  for name, t in node_type.items() if t == "&"}
    seen = {n: [] for n, conns in node_connections.items() if combiner_node in conns}
    for i in count(1):
        for from_m, to_m, p in run(node_type, node_connections, flip_state, conj_state, ("button", "roadcaster", LOW)):
            if p == HIGH and to_m == combiner_node:
                seen[from_m].append(i)
                if all(len(x) >= 1 for x in seen.values()):
                    return reduce(math.lcm, (x[0] for x in seen.values()))


def solve(inp, part1):
    node_type = {}
    node_connections = {}
    for l in inp.splitlines():
        name, conns = l.split(" -> ")
        ntype, name = name[0], name[1:]
        node_type[name] = ntype
        node_connections[name] = conns.split(", ")
    if part1:
        return solve_part1(node_type, node_connections)
    else:
        return solve_part2(node_type, node_connections)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
