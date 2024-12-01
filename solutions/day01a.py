import numpy as np

x = np.fromfile("day01input.txt", dtype=int, sep=" ")
x = x.reshape((x.size // 2, 2))
print(sum(np.abs(np.sort(x[:, 0]) - np.sort(x[:, 1]))))
