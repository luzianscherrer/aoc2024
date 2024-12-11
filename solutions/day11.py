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
