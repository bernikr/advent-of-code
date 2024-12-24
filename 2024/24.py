from collections.abc import Iterable


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


def solve(inp: str) -> Iterable[tuple[int, int | str]]:
    inputs, gates = inp.split("\n\n")
    inputs = {a[:3]: a[5] == "1" for a in inputs.splitlines()}
    if len(inputs) != 90:
        msg = "Input does not use 45-bit inputs"
        raise ValueError(msg)
    gates = {a[-3:]: (a[4:-11], a[:3], a[-10:-7]) for a in gates.splitlines()}
    yield 1, sum(1 << int(a[1:]) for a in gates if a[0] == "z" and get_gate_value(a, inputs, gates))


if __name__ == "__main__":
    from aocd import AocdError, data, submit

    try:
        for part, solution in solve(data):
            submit(solution, part=("a", "b")[part - 1])
    except AocdError as e:
        print(e)
