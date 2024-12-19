import heapq
from functools import cache

data = open("day19input.txt").read().split("\n")

patterns = data[0].split(", ")
data = data[2:]


@cache
def all_solutions(current):
    if current:
        count = 0
        for pattern in patterns:
            if current.startswith(pattern):
                count += all_solutions(current[len(pattern) :])
        return count
    else:
        return 1


count1, count2 = 0, 0
for i, current in enumerate(data):
    heap = []
    heapq.heappush(heap, (len(current), ""))
    while len(heap):
        candidate = heapq.heappop(heap)
        pos = candidate[0]
        if pos == 0:
            count1 += 1
            break
        for pattern in patterns:
            if current[-pos:].startswith(pattern) and pos - len(pattern) >= 0:
                heapq.heappush(heap, (pos - len(pattern), pattern))
    count2 += all_solutions(current)

print(count1, count2)
