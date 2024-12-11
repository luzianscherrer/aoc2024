from collections import defaultdict


def process(lst):
    res = []
    for num in lst:
        if num == 0:
            res.append(1)
        elif len(str(num)) % 2 == 0:
            length = len(str(num))
            res.append(int(str(num)[0 : length // 2]))
            res.append(int(str(num)[length // 2 :]))
        else:
            res.append(num * 2024)
    return res


total = 0
values = open("day11input.txt").readline().split(" ")
for value in values:
    current = [int(value)]
    for _ in range(25):
        current = process(current)
    total += len(current)
print(total)


# ---

# d = defaultdict(int)

# values = open("day11example.txt").readline().split(" ")
# for val in values:
#     d[int(val)] = 1

# # print(d)

# for _ in range(6):
#     for key in list(d):
#         # print(key, d[key])
#         if d[key] > 0:
#             num = d[key]
#             d[key] = 0
#             res = process([key])
#             # print(res)
#             for val in res:
#                 d[val] += num
#                 # print(val)
#     print(d)
#     input()
# sum = 0
# for key, value in d.items():
#     sum += value
# print(sum)
