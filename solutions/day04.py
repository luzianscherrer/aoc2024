import numpy as np
import re

a = np.genfromtxt("day04input.txt", dtype=str, delimiter=1)

# part 1
str = ""
for i in range(4):
    for j in range(a.shape[0]):
        str += "".join(a[j, :]) + ","
    for j in range(-a.shape[0] + 1, a.shape[0]):
        str += "".join(a.diagonal(j)) + ","
    a = np.rot90(a)
print(len(re.findall(r"XMAS", str)))

# part 2
a = np.pad(a, 1)
res = 0
for y in range(1, a.shape[0] - 1):
    for x in range(1, a.shape[1] - 1):
        res += (
            a[y, x] == "A"
            and (
                (a[y - 1, x - 1] == "M" and a[y + 1, x + 1] == "S")
                or (a[y - 1, x - 1] == "S" and a[y + 1, x + 1] == "M")
            )
            and (
                (a[y - 1, x + 1] == "M" and a[y + 1, x - 1] == "S")
                or (a[y - 1, x + 1] == "S" and a[y + 1, x - 1] == "M")
            )
        )
print(res)
