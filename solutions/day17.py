import re

data = open("day17input.txt").read().replace("\n", "")
match = re.search(r"A: (\d+).+B: (\d+).+C: (\d+).+m: (.+)", data)
reg_a, reg_b, reg_c = int(match.group(1)), int(match.group(2)), int(match.group(3))
prg = match.group(4).split(",")


def combo(value, a, b, c):
    return (list(range(4)) + [a, b, c])[value]


def run(a, b, c, prg):
    i = 0
    output = []
    while i < len(prg) - 1:
        opcode, operand = int(prg[i]), int(prg[i + 1])
        if opcode == 0:
            a = a // (2 ** combo(operand, a, b, c))
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo(operand, a, b, c) % 8
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(combo(operand, a, b, c) % 8)
        elif opcode == 6:
            b = a // (2 ** combo(operand, a, b, c))
        elif opcode == 7:
            c = a // (2 ** combo(operand, a, b, c))
        i += 2
    return ",".join(map(str, output))


print(run(reg_a, reg_b, reg_c, prg))

cand = [0]
for lng in range(1, len(list(map(int, prg))) + 1):
    cand_before = cand
    cand = []
    for value in cand_before:
        for offset in range(8):
            value_a = 8 * value + offset
            if run(value_a, reg_b, reg_c, prg) == ",".join(prg[-lng:]):
                cand.append(value_a)

print(min(cand))
