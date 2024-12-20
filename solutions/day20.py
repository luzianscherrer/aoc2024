import numpy as np
import networkx as nx

M = np.genfromtxt("day20input.txt", dtype=str, comments="_", delimiter=1)
G = nx.Graph()
dirs = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
walls = []


def connect_pos(y, x):
    for dir in dirs:
        if M[tuple([y, x] + dir)] in [".", "S", "E"]:
            G.add_edge(f"{y},{x}", f"{y+dir[0]},{x+dir[1]}")


for y in range(1, M.shape[0] - 1):
    for x in range(1, M.shape[1] - 1):
        if M[y, x] == "E":
            end = f"{y},{x}"
        elif M[y, x] == "S":
            start = f"{y},{x}"
        if M[y, x] == "#":
            walls.append([y, x])
            continue
        connect_pos(y, x)


base_length = nx.shortest_path_length(G, start, end)

count = 0
for i, wall in enumerate(walls):
    print(f"{i} of {len(walls)}")
    G_orig = G.copy()
    connect_pos(*wall)
    this_length = nx.shortest_path_length(G, start, end)
    count += base_length - this_length >= 100
    G = G_orig
print(count)
