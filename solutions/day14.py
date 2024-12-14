import re
import numpy as np
from scipy.signal import convolve


def part1(m, p):
    cy, cx = m[0] // 2, m[1] // 2
    res = np.zeros(4)
    res[0] = np.sum((p[:, 0] < cy) & (p[:, 1] < cx))
    res[1] = np.sum((p[:, 0] > cy) & (p[:, 1] < cx))
    res[2] = np.sum((p[:, 0] < cy) & (p[:, 1] > cx))
    res[3] = np.sum((p[:, 0] > cy) & (p[:, 1] > cx))
    print(f"part1: {int(np.prod(res))}")


def part2_display(m, p):
    v = np.zeros(m)
    v[p[:, 0], p[:, 1]] = 1
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    print(re.sub(r"[ .\[\]]", "", str(v)))


data = open("day14input.txt").read().split("\n")
p = np.zeros((len(data), 2), dtype=int)
v = np.zeros_like(p)

for i, line in enumerate(data):
    match = re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
    p[i] = [int(match.group(2)), int(match.group(1))]
    v[i] = [int(match.group(4)), int(match.group(3))]

searchlen = 10
kernel = np.ones(searchlen)
lengths = np.array([p[:, 0].max() + 1, p[:, 1].max() + 1]).astype(int)
i, found = 0, False
while not found:
    if i == 100:
        part1(lengths, p)
    p = (p + v) % lengths
    i += 1
    matrix = np.zeros(lengths)
    matrix[p[:, 0], p[:, 1]] = 1
    for row in matrix:
        if np.any(convolve(row, kernel, mode="valid") == searchlen):
            found = True
            part2_display(lengths, p)
            print(f"part2: {i}")
            break
