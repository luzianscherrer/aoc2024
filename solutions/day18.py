import numpy as np
import networkx as nx


def build_graph(data, field_size, bytes_limit):
    G = nx.Graph()
    M = np.ones((field_size + 1, field_size + 1))
    count = 1
    for line in data:
        x, y = map(int, line.split(","))
        M[y, x] = 0
        if count == bytes_limit:
            break
        count += 1

    M = np.pad(M, 1)
    dirs = np.array([[1, 0], [1, 0], [0, -1], [-1, 0]])
    for y in range(1, M.shape[0] - 1):
        for x in range(1, M.shape[1] - 1):
            if M[tuple([y, x])] == 0:
                continue
            for dir in dirs:
                if M[tuple([y, x] + dir)]:
                    G.add_edge(f"{y-1},{x-1}", f"{y-1+dir[0]},{x-1+dir[1]}")
    return G


field_size = 70
bytes_limit = 1024
data = open("day18input.txt").read().split("\n")
G = build_graph(data, field_size, bytes_limit)
print(nx.shortest_path_length(G, "0,0", f"{field_size},{field_size}"))

while True:
    bytes_limit += 1
    G = build_graph(data, field_size, bytes_limit)
    try:
        nx.shortest_path_length(G, "0,0", f"{field_size},{field_size}")
    except nx.NetworkXNoPath:
        print(data[bytes_limit - 1])
        break
