import numpy as np

# data = np.genfromtxt("day22input.txt", dtype=int)

# for _ in range(2000):
#     data = ((data * 64) ^ data) % 16777216
#     data = ((data // 32) ^ data) % 16777216
#     data = ((data * 2048) ^ data) % 16777216

# print(sum(data))

num = 2000

data = np.genfromtxt("day22input.txt", dtype=int)
# data = np.array([1, 2, 3, 2024], dtype=int)

res = np.zeros((num, len(data)), dtype=int)

for i in range(num):
    res[i] = data % 10
    data = ((data * 64) ^ data) % 16777216
    data = ((data // 32) ^ data) % 16777216
    data = ((data * 2048) ^ data) % 16777216

diffs = np.diff(res, axis=0)


seqs = set()
for buyer in range(diffs.shape[1]):
    print("building sequences... buyer", buyer)

    for i in range(len(diffs[:, buyer]) - 3):
        sub = diffs[:, buyer][i : i + 4]
        seqs.add(tuple(sub))

best = 0
for j, seq in enumerate(seqs):
    print(f"{j} of {len(seqs)}")
    testseq = np.array(seq, dtype=int)

    total = 0
    for buyer in range(diffs.shape[1]):
        # print(f"calculating for seq {j} of {len(seqs)} buyer", buyer)

        for i in range(len(diffs[:, buyer]) - 3):
            sub = diffs[:, buyer][i : i + 4]
            if (sub == testseq).all():
                total += res[i + 4, buyer]
                break

    print("current", total)
    best = max(best, total)
    print("best", best)
