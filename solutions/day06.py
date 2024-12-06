import numpy as np

a = np.pad(
    np.genfromtxt(
        "day06input.txt", dtype=str, deletechars="", comments="_", delimiter=1
    ),
    1,
)
a = np.pad(a, 1)
y, x = np.hstack((a == "^").nonzero())
while a[y - 1, x] != "0":
    if a[y - 1, x] == "#":
        a = np.rot90(a)
        y, x = np.hstack((a == "^").nonzero())
    else:
        a[y, x] = "X"
        y -= 1
        a[y, x] = "^"

print(1 + sum((a == "X").flatten()))
