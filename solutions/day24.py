wires = {}
operations = []


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


data = open("day24input.txt").read().split("\n")
for line in data:
    if ":" in line:
        wire, value = line.split(": ")
        wires[wire] = int(value)
    elif "->" in line:
        op1, op, op2, _, res = line.split(" ")
        operations.append((op1, op, op2, res))

while len(operations):
    op1, op, op2, res = operations.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        operations.append((op1, op, op2, res))

bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
print(int("".join(bits), 2))
