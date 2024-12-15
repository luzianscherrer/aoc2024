import numpy as np
from io import StringIO

data = open("day15input.txt").read().split("\n\n")
field = np.genfromtxt(
    StringIO(data[0]), dtype=str, deletechars="", comments="_", delimiter=1
)


def print_field(field):
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    print(
        str(field)
        .replace(" ", "")
        .replace("'", "")
        .replace("[[", "[")
        .replace("]]", "]")
    )


def print_result(symbol):
    result = (field == symbol).nonzero()
    print(np.sum(result[0] * 100) + np.sum(result[1]))


# part 1
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

print_result("O")

# part 2
data[0] = (
    data[0].replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
)
field = np.genfromtxt(
    StringIO(data[0]), dtype=str, deletechars="", comments="_", delimiter=1
)

for move in data[1].replace("\n", ""):
    pos = np.hstack((field == "@").nonzero())

    if move in ["<", ">"]:
        if move == "<":
            ahead = field[pos[0], pos[1] :: -1]
        elif move == ">":
            ahead = field[pos[0], pos[1] :]

        linepos, linelen = 0, 1
        for i in range(1, len(ahead)):
            if ahead[i] == ".":
                for j in range(linelen):
                    ahead[i - j] = ahead[i - 1 - j]
                ahead[linepos] = "."
                linepos += 1
                break
            elif ahead[i] == "[" or ahead[i] == "]":
                linelen += 1
            elif ahead[i] == "#":
                break

    elif move in ["^", "v"]:
        if move == "^":
            dir = [-1, 0]
        elif move == "v":
            dir = [1, 0]

        if field[tuple(pos + dir)] == ".":
            field[tuple(pos + dir)] = "@"
            field[tuple(pos)] = "."
        elif field[tuple(pos + dir)] in ["[", "]"]:
            cand = [pos + dir]
            cluster = []
            while len(cand):
                check = cand.pop(0)
                if field[tuple(check)] == "]":
                    cluster += [check, check + [0, -1]]
                    cand += [check + [dir[0], 0], check + [dir[0], -1]]
                elif field[tuple(check)] == "[":
                    cluster += [check, check + [0, 1]]
                    cand += [check + [dir[0], 0], check + [dir[0], 1]]
            cluster = [np.array(item) for item in {tuple(arr) for arr in cluster}]
            blocked = False
            for element in cluster:
                if field[tuple(element + dir)] == "#":
                    blocked = True
                    break
            if not blocked:
                for element in sorted(cluster, key=lambda x: x[0], reverse=dir[0] + 1):
                    field[tuple(element + dir)] = field[tuple(element)]
                    field[tuple(element)] = "."
                field[tuple(pos + dir)] = "@"
                field[tuple(pos)] = "."

print_result("[")
