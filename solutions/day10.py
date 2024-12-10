import numpy as np
import networkx as nx

field = np.genfromtxt("day10input.txt", dtype=int, delimiter=1)
field = np.pad(field, 1, constant_values=-1)

G = nx.DiGraph()
startnodes = []

directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
for y in range(1, field.shape[0] - 1):
    for x in range(1, field.shape[1] - 1):
        G.add_node(f"{y},{x}")
        if field[y, x] == 0:
            startnodes.append(f"{y},{x}")
        for direction in directions:
            if field[tuple(direction + [y, x])] - field[y, x] == 1:
                G.add_edge(f"{y},{x}", f"{y+direction[0]},{x+direction[1]}")

sum = 0
for startnode in startnodes:
    sum += len(
        list(
            filter(
                lambda a: a[1] == 9,
                nx.single_source_shortest_path_length(G, startnode).items(),
            )
        )
    )
print(sum)
