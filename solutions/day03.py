import re

res, valid = [0, 0], 1
with open("day03input.txt") as file:
    line = file.read()
    for match in re.findall(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))", line):
        if match[0]:
            valid = 1
        elif match[1]:
            valid = 0
        else:
            x = int(match[3]) * int(match[4])
            res[0] += x
            res[1] += x * valid
print(res)
