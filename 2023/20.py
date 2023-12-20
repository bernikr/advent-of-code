import math
from collections import deque
from functools import reduce
from itertools import count

HIGH, LOW = True, False
ON, OFF = True, False


def get_initial_state(graph):
    node_type, node_connections = graph
    flip_state = {name: OFF for name, t in node_type.items() if t == "%"}
    conj_state = {name: {n: LOW for n, conns in node_connections.items() if name in conns}
                  for name, t in node_type.items() if t == "&"}
    return flip_state, conj_state


def run(graph, state):
    node_type, node_connections = graph
    flip_state, conj_state = state
    msg_queue = deque()
    msg_queue.append(("button", "roadcaster", LOW))
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


def solve_part1(graph):
    state = get_initial_state(graph)
    pulses = [0, 0]
    for _ in range(1000):
        for _, _, p in run(graph, state):
            pulses[p] += 1

    return pulses[0] * pulses[1]


def solve_part2(graph):
    node_type, node_connections = graph
    # assume that there is exactly one & node before rx whose inputs all have a simple periodicity
    # simple = turn on every x button pushes
    combiner_node = [n for n, conns in node_connections.items() if "rx" in conns]
    assert len(combiner_node) == 1 and node_type[combiner_node[0]] == "&"
    combiner_node = combiner_node[0]

    state = get_initial_state(graph)
    seen = {n: 0 for n, conns in node_connections.items() if combiner_node in conns}
    for i in count(1):
        for from_m, to_m, p in run(graph, state):
            if p == HIGH and to_m == combiner_node:
                if not seen[from_m]:
                    seen[from_m] = i
                if all(x for x in seen.values()):
                    return reduce(math.lcm, seen.values())


def solve(inp, part1):
    node_type = {}
    node_connections = {}
    for l in inp.splitlines():
        name, conns = l.split(" -> ")
        ntype, name = name[0], name[1:]
        node_type[name] = ntype
        node_connections[name] = conns.split(", ")
    graph = node_type, node_connections
    if part1:
        return solve_part1(graph)
    else:
        return solve_part2(graph)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
