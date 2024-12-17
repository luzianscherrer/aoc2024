import re

data = open("day17input.txt").read().replace("\n", "")
match = re.search(r"A: (\d+).+B: (\d+).+C: (\d+).+m: (.+)", data)
reg_a = int(match.group(1))
reg_b = int(match.group(2))
reg_c = int(match.group(3))
prg = match.group(4).split(",")
ip = 0
output = []


def combo(value):
    if value == 4:
        return reg_a
    elif value == 5:
        return reg_b
    elif value == 6:
        return reg_c
    return value


while ip < len(prg) - 1:
    opcode = int(prg[ip])
    operand = int(prg[ip + 1])
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

print(reg_a, reg_b, reg_c)
print(",".join(map(str, output)))
