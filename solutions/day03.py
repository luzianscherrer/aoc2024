import re

res = [0, 0]
with open("day03input.txt") as file:
    line = file.read()
    res[0] = sum(
        [int(i[0]) * int(i[1]) for i in re.findall(r"mul\((\d+),(\d+)\)", line)]
    )
print(res)
