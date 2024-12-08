import numpy as np
from itertools import combinations

field = np.genfromtxt("day08input.txt", dtype=str, delimiter=1)
pos = {}
res = np.zeros(field.shape)


def set(y, x):
    if y >= 0 and x >= 0 and y < field.shape[0] and x < field.shape[1]:
        res[y, x] = 1


for symbol in np.unique(field):
    if symbol == ".":
        continue
    pos[symbol] = list(zip(*(field == symbol).nonzero()))

for symbol in pos:
    for pair in combinations(pos[symbol], 2):
        slope = (pair[0][1] - pair[1][1]) / (pair[0][0] - pair[1][0])
        dist = pair[1][0] - pair[0][0]
        set(pair[0][0] - dist, pair[0][1] - int(dist * slope))
        set(pair[1][0] + dist, pair[1][1] + int(dist * slope))

print(int(np.sum(res)))
