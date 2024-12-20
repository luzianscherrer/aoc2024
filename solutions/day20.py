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
dist = 100

count1 = 0
for i, wall in enumerate(walls):
    if i % 100 == 0:
        print(f"part1 {i/len(walls)*100:.0f}%")
    G_orig = G.copy()
    connect_pos(*wall)
    this_length = nx.shortest_path_length(G, start, end)
    count1 += base_length - this_length >= dist
    G = G_orig
print("part1 done")

shortest_path = nx.shortest_path(G, start, end)
shortest_path_int = np.array(
    [list(map(int, node.split(","))) for node in shortest_path]
)

count2 = 0
for i in range(len(shortest_path_int)):
    if i % 100 == 0:
        print(f"part2 {i/len(shortest_path_int)*100:.0f}%")
    j = i + dist
    while j < len(shortest_path_int):
        l1_dist = np.linalg.norm(
            shortest_path_int[i] - shortest_path_int[j],
            ord=1,
        )
        if l1_dist <= 20 and j - i - l1_dist >= dist:
            count2 += 1
        j += 1
print("part2 done")

print(f"part1: {count1}, part2: {count2}")
