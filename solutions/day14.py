import re
import numpy as np

input = open("day14input.txt").read().split("\n")
p = np.zeros((len(input), 2))
v = np.zeros_like(p)

for i, line in enumerate(input):
    match = re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
    p[i] = [int(match.group(2)), int(match.group(1))]
    v[i] = [int(match.group(4)), int(match.group(3))]

m = np.array([p[:, 0].max() + 1, p[:, 1].max() + 1])

for _ in range(100):
    p = (p + v) % m

res = np.zeros(4)
for pos in p:
    if pos[0] < m[0] // 2 and pos[1] < m[1] // 2:
        res[0] += 1
    elif pos[0] > m[0] // 2 and pos[1] < m[1] // 2:
        res[1] += 1
    elif pos[0] < m[0] // 2 and pos[1] > m[1] // 2:
        res[2] += 1
    elif pos[0] > m[0] // 2 and pos[1] > m[1] // 2:
        res[3] += 1

print(int(np.prod(res)))
