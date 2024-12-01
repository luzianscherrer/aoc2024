import numpy as np

x = np.fromfile("day01input.txt", dtype=int, sep=" ")
x = x.reshape((x.size // 2, 2))
print(sum([n * sum(x[:, 1] == n) for n in x[:, 0]]))
