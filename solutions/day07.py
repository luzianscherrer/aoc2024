from itertools import product

part1, part2 = 0, 0
recheck = []
with open("day07input.txt") as file:
    operators = ["+", "*"]
    for line in file:
        result, operands = line.split(":")
        operands = operands.split()
        valid = False
        for opt in product(operators, repeat=len(operands) - 1):
            lst = list(zip(operands, [""] + list(opt)))
            res = lst[0][0]
            for sub in lst[1:]:
                res = eval(f"{res}{sub[1]}{sub[0]}")
            if int(result) == res:
                part1 += res
                valid = True
                break
        if not valid:
            recheck.append([result, operands])

operators.append("||")
for result, operands in recheck:
    for opt in product(operators, repeat=len(operands) - 1):
        if "||" not in opt:
            continue
        lst = list(zip(operands, [""] + list(opt)))
        res = lst[0][0]
        for sub in lst[1:]:
            if sub[1] == "||":
                res = int(f"{res}{sub[0]}")
            else:
                res = eval(f"{res}{sub[1]}{sub[0]}")
        if int(result) == res:
            part2 += res
            break

print(part1, part1 + part2)
