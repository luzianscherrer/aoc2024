import numpy as np

x = np.loadtxt("day01input.txt", dtype=int)
print(sum(np.abs(np.sort(x[:, 0]) - np.sort(x[:, 1]))))
