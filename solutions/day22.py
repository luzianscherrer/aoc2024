import numpy as np

data = np.genfromtxt("day22input.txt", dtype=int)

for _ in range(2000):
    data = ((data * 64) ^ data) % 16777216
    data = ((data // 32) ^ data) % 16777216
    data = ((data * 2048) ^ data) % 16777216

print(sum(data))
