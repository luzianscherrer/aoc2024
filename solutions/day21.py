import networkx as nx
import numpy as np


def get_paths(keypad, code):
    G = nx.DiGraph()
    keypad = np.pad(keypad, 1, constant_values="")

    dirs = {">": [0, 1], "v": [1, 0], "<": [0, -1], "^": [-1, 0]}
    for y in range(1, keypad.shape[0] - 1):
        for x in range(1, keypad.shape[1] - 1):
            if len(keypad[y, x]):
                for k, v in dirs.items():
                    if len(keypad[tuple(np.array([y, x]) + v)]):
                        G.add_edge(
                            keypad[y, x], keypad[tuple(np.array([y, x]) + v)], dir=k
                        )

    best_paths = [""]
    code = "A" + code
    for i in range(len(code) - 1):
        new_paths = []
        paths = list(nx.all_shortest_paths(G, code[i], code[i + 1]))
        for path in paths:
            path_desc = [G[a][b]["dir"] for a, b in zip(path[:-1], path[1:])]
            for known in best_paths:
                new_paths.append(known + "".join(path_desc) + "A")
        best_paths = new_paths

    return best_paths


numpad = np.array([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]])
dirpad = np.array([["", "^", "A"], ["<", "v", ">"]])


data = open("day21input.txt").read().split("\n")
res = 0
for code in data:
    paths = get_paths(numpad, code)
    for i in range(2):
        new_paths = []
        for path in paths:
            new_paths += get_paths(dirpad, path)
        paths = new_paths

    res += int(code.replace("A", "")) * min([len(path) for path in paths])

print(res)
