from collections.abc import Iterable
from itertools import chain, product

import networkx as nx
from tqdm import tqdm

INPUT_BIT_LENGTH = 45


def get_gate_value(wire: str, inputs: dict[str, bool], gate: dict[str, tuple[str, str, str]]) -> bool:
    if wire in inputs:
        return inputs[wire]
    op, a, b = gate[wire]
    if op == "AND":
        return get_gate_value(a, inputs, gate) and get_gate_value(b, inputs, gate)
    if op == "OR":
        return get_gate_value(a, inputs, gate) or get_gate_value(b, inputs, gate)
    if op == "XOR":
        return get_gate_value(a, inputs, gate) ^ get_gate_value(b, inputs, gate)
    msg = f"Unknown operation {op}"
    raise NotImplementedError(msg)


def build_ripple_carry_adder(input_bit_length: int) -> nx.DiGraph:
    g = nx.DiGraph()

    # half-adder for bit 0
    g.add_node("z00", op="XOR")
    g.add_node("c00", op="AND")
    g.add_edges_from([("x00", "z00"), ("y00", "z00"), ("x00", "c00"), ("y00", "c00")])

    for i in range(1, input_bit_length):
        # full adder for bit i
        x = f"x{i:02}"
        y = f"y{i:02}"
        z = f"z{i:02}"
        ci = f"c{i - 1:02}"
        co = f"c{i:02}"
        i1 = f"1{i:02}"
        i2 = f"2{i:02}"
        i3 = f"3{i:02}"
        g.add_node(i1, op="XOR")
        g.add_node(z, op="XOR")
        g.add_node(i2, op="AND")
        g.add_node(i3, op="AND")
        g.add_node(co, op="OR")
        g.add_edges_from([(x, i1), (y, i1), (i1, z), (ci, z), (x, i2), (y, i2), (i1, i3), (ci, i3), (i2, co), (i3, co)])
    return nx.relabel_nodes(g, {f"c{input_bit_length - 1:02}": f"z{input_bit_length:02}"}, copy=False)


def split_gates(g: nx.DiGraph) -> nx.DiGraph:
    gates = {n for n, attr in g.nodes.items() if "op" in attr}
    g = nx.relabel_nodes(g, {n: f">{n}" for n in gates}, copy=False)
    for n in gates:
        nn = f">{n}"
        for neigh in list(g.neighbors(nn)):
            g.add_edge(n, neigh)
            g.remove_edge(nn, neigh)
        g.add_edge(nn, n, inner=True)
    for n in g.nodes:
        if n.startswith(("x", "y", "z")):
            g.nodes[n]["name"] = n
    return g


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inputs, gates = inp.split("\n\n")
    inputs = {a[:3]: a[5] == "1" for a in inputs.splitlines()}
    gates = {a[-3:]: (a[4:-11], a[:3], a[-10:-7]) for a in gates.splitlines()}
    yield 1, sum(1 << int(a[1:]) for a in gates if a[0] == "z" and get_gate_value(a, inputs, gates))

    g1 = nx.DiGraph()
    for a, (op, b, c) in gates.items():
        g1.add_node(a, op=op)
        g1.add_edge(b, a)
        g1.add_edge(c, a)

    input_bit_length = len(inputs) // 2
    g2 = build_ripple_carry_adder(input_bit_length)

    xs = {x for x in g1.nodes if x.startswith("x")}
    ys = {y for y in g2.nodes if y.startswith("y")}
    zs = {z for z in g2.nodes if z.startswith("z")}

    swap_candidates = set(gates)
    for xy, z in tqdm(product(chain(xs, ys), zs)):
        for p1, p2 in zip(
                sorted(nx.all_simple_paths(g1, xy, z), key=len),
                sorted(nx.all_simple_paths(g2, xy, z), key=len),
        ):
            if len(p1) != len(p2):
                continue
            if all(g1.nodes[n1]["op"] == g2.nodes[n2]["op"] for n1, n2 in zip(p1[1:], p2[1:])):
                swap_candidates -= set(p1)
    print(len(swap_candidates))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
