import re

res, valid = [0, 0], 1
line = open("day03input.txt").read()
regex = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"
for match in re.findall(regex, line):
    if match[0]:
        valid = 1
    elif match[1]:
        valid = 0
    else:
        x = int(match[3]) * int(match[4])
        res[0] += x
        res[1] += x * valid
print(res)
