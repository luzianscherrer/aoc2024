import heapq

data = open("day19input.txt").read().split("\n")

patterns = data[0].split(", ")
data = data[2:]

count = 0
for i, current in enumerate(data):
    heap = []
    heapq.heappush(heap, (len(current), ""))
    while len(heap):
        candidate = heapq.heappop(heap)
        pos = candidate[0]
        if pos == 0:
            count += 1
            break
        for pattern in patterns:
            if current[-pos:].startswith(pattern):
                heapq.heappush(heap, (pos - len(pattern), pattern))

print(count)
