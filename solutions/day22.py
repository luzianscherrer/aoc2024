import numpy as np

data = np.genfromtxt("day22input.txt", dtype=int)
rounds = 2000
res = np.zeros((rounds, len(data)), dtype=int)
for i in range(2000):
    res[i] = data % 10
    data = ((data * 64) ^ data) % 16777216
    data = ((data // 32) ^ data) % 16777216
    data = ((data * 2048) ^ data) % 16777216
print(sum(data))

diffs = np.diff(res, axis=0)
seqs = {}
for buyer in range(diffs.shape[1]):
    for i in range(len(diffs[:, buyer]) - 3):
        sub = diffs[:, buyer][i : i + 4]
        if tuple(sub) not in seqs:
            seqs[tuple(sub)] = np.zeros(len(data), dtype=int)
        if seqs[tuple(sub)][buyer] == 0:
            seqs[tuple(sub)][buyer] = res[i + 4, buyer]

best = 0
for k, v in seqs.items():
    best = max(best, sum(v))
print(best)
