import networkx as nx
import numpy as np
from functools import cache

dirs = {">": [0, 1], "v": [1, 0], "<": [0, -1], "^": [-1, 0]}
numpad = np.array([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]])
dirpad = np.array([["", "^", "A"], ["<", "v", ">"]])


def get_paths(keypad, code):
    G = nx.DiGraph()
    keypad = np.pad(keypad, 1, constant_values="")

    for y in range(1, keypad.shape[0] - 1):
        for x in range(1, keypad.shape[1] - 1):
            if len(keypad[y, x]):
                for k, v in dirs.items():
                    if len(keypad[tuple(np.array([y, x]) + v)]):
                        G.add_edge(
                            keypad[y, x], keypad[tuple(np.array([y, x]) + v)], dir=k
                        )

    best_paths = [""]
    for i in range(len(code) - 1):
        new_paths = []
        paths = list(nx.all_shortest_paths(G, code[i], code[i + 1]))
        for path in paths:
            path_desc = [G[a][b]["dir"] for a, b in zip(path[:-1], path[1:])]
            for known in best_paths:
                new_paths.append(known + "".join(path_desc) + "A")
        best_paths = new_paths

    return best_paths


@cache
def resolve(code, distance):
    res = 0
    code = "A" + code
    for i in range(1, len(code)):
        paths = get_paths(dirpad, code[i - 1 : i + 1])
        if distance == 0:
            res += min([len(path) for path in paths])
        else:
            res += min(resolve(path, distance - 1) for path in paths)
    return res


def run(code, steps):
    return min([resolve(x, steps - 1) for x in get_paths(numpad, "A" + code)])


data = open("day21input.txt").read().split("\n")
res1, res2 = 0, 0
for code in data:
    res1 += int(code.replace("A", "")) * run(code, 2)
    res2 += int(code.replace("A", "")) * run(code, 25)

print(res1, res2)
