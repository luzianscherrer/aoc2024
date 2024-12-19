data = open("day19input.txt").read().split("\n")

patterns = data[0].split(", ")
data = data[2:]

count = 0
for i, current in enumerate(data):
    print(f"processing {i} of {len(data)}")
    candidates = [["", 0]]
    while len(candidates):
        candidate = candidates.pop(0)
        pos = candidate[1]

        if pos == len(current):
            count += 1
            break

        for pattern in patterns:
            if current[pos:].startswith(pattern):
                candidates.append([pattern, pos + len(pattern)])


print(count)
