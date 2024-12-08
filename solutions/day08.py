import numpy as np
from itertools import combinations

field = np.genfromtxt("day08input.txt", dtype=str, delimiter=1)
pos = {}
res = np.zeros(field.shape, dtype=int)


def mark(y, x, val):
    if y >= 0 and x >= 0 and y < field.shape[0] and x < field.shape[1]:
        res[y, x] |= val
        return True
    return False


for symbol in np.unique(field):
    if symbol != ".":
        for pair in combinations(zip(*(field == symbol).nonzero()), 2):
            slope = (pair[0][1] - pair[1][1]) / (pair[0][0] - pair[1][0])
            odist = dist = pair[1][0] - pair[0][0]
            val = 1
            while mark(pair[0][0] - dist, pair[0][1] - int(dist * slope), val):
                dist += odist
                val = 2
            dist = odist
            val = 1
            while mark(pair[1][0] + dist, pair[1][1] + int(dist * slope), val):
                dist += odist
                val = 2
            res[pair[0]] |= 2
            res[pair[1]] |= 2

print(np.sum(res & 1), np.sum(res > 0))
