import numpy as np

x = np.loadtxt("day01input.txt", dtype=int)
print(sum([n * sum(x[:, 1] == n) for n in x[:, 0]]))
