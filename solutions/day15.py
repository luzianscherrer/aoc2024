import numpy as np
from io import StringIO

data = open("day15input.txt").read().split("\n\n")
field = np.genfromtxt(
    StringIO(data[0]), dtype=str, deletechars="", comments="_", delimiter=1
)

for move in data[1].replace("\n", ""):
    pos = np.hstack((field == "@").nonzero())

    if move == "<":
        ahead = field[pos[0], pos[1] :: -1]
    elif move == "^":
        ahead = field[pos[0] :: -1, pos[1]]
    elif move == ">":
        ahead = field[pos[0], pos[1] :]
    elif move == "v":
        ahead = field[pos[0] :, pos[1]]

    linepos, linelen = 0, 1
    for i in range(1, len(ahead)):
        if ahead[i] == ".":
            for j in range(linelen):
                ahead[i - j] = ahead[i - 1 - j]
            ahead[linepos] = "."
            linepos += 1
            break
        elif ahead[i] == "O":
            linelen += 1
        elif ahead[i] == "#":
            break

result = (field == "O").nonzero()
print(np.sum(result[0] * 100) + np.sum(result[1]))
