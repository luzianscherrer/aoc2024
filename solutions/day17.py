import re

data = open("day17input.txt").read().replace("\n", "")
match = re.search(r"A: (\d+).+B: (\d+).+C: (\d+).+m: (.+)", data)
reg_a, reg_b, reg_c = int(match.group(1)), int(match.group(2)), int(match.group(3))
prg, ip, output = match.group(4).split(","), 0, []


def combo(value):
    return (list(range(4)) + [reg_a, reg_b, reg_c])[value]


while ip < len(prg) - 1:
    opcode, operand = int(prg[ip]), int(prg[ip + 1])
    if opcode == 0:
        reg_a = reg_a // (2 ** combo(operand))
    elif opcode == 1:
        reg_b = reg_b ^ operand
    elif opcode == 2:
        reg_b = combo(operand) % 8
    elif opcode == 3:
        if reg_a != 0:
            ip = operand
            continue
    elif opcode == 4:
        reg_b = reg_b ^ reg_c
    elif opcode == 5:
        output.append(combo(operand) % 8)
    elif opcode == 6:
        reg_b = reg_a // (2 ** combo(operand))
    elif opcode == 7:
        reg_c = reg_a // (2 ** combo(operand))
    ip += 2

print(",".join(map(str, output)))
