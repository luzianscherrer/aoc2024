import numpy as np
import re

a = np.genfromtxt("day04input.txt", dtype=str, delimiter=1)

# part 1
str = ""
dim = a.shape[0]
for i in range(4):
    str += ",".join(["".join(a[j, :]) for j in range(dim)])
    str += ",".join(["".join(a.diagonal(j)) for j in range(-dim + 1, dim)])
    a = np.rot90(a)
print(len(re.findall(r"XMAS", str)))

# part 2
count = 0
a = np.pad(a, 1)
for y in range(1, a.shape[0] - 1):
    for x in range(1, a.shape[1] - 1):
        count += (
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
print(count)
