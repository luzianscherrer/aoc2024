import numpy as np
import networkx as nx

M = np.genfromtxt("day16input.txt", dtype=str, comments="_", delimiter=1)
G = nx.DiGraph()
dirs = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])


def bi_add_edge(a, b, weight, miss):
    for _ in range(2):
        G.add_edge(
            f"{a[0]},{a[1]}",
            f"{b[0]},{b[1]}",
            weight=weight,
            miss=f"{miss[0]},{miss[1]}",
        )
        b, a = a, b


for y in range(M.shape[0]):
    for x in range(M.shape[1]):
        if M[y, x] == "E":
            end = f"{y},{x}"
        elif M[y, x] == "S":
            start = f"{y},{x}"
            startpos = [y, x]
        if M[y, x] == "#":
            continue
        ns = []
        for pos in dirs:
            if M[tuple([y, x] + pos)] in [".", "S", "E"]:
                ns.append([y, x] + pos)

        if len(ns) == 1:
            G.add_edge(f"{y},{x}", f"{ns[0][0]},{ns[0][1]}", weight=1)

        elif len(ns) == 2:
            if ns[0][0] == ns[1][0] or ns[0][1] == ns[1][1]:
                for n in ns:
                    G.add_edge(f"{y},{x}", f"{n[0]},{n[1]}", weight=1)
            else:
                for n in ns:
                    G.add_edge(f"{n[0]},{n[1]}", f"{y},{x}", weight=1)
                bi_add_edge(ns[0], ns[1], 1002, [y, x])

        elif len(ns) == 3:
            for n in ns:
                G.add_edge(f"{n[0]},{n[1]}", f"{y},{x}", weight=1)
            if ns[0][0] == ns[2][0]:
                ns[1], ns[2] = ns[2], ns[1]
            elif ns[1][0] == ns[2][0]:
                ns[0], ns[2] = ns[2], ns[0]
            elif ns[0][1] == ns[2][1]:
                ns[1], ns[2] = ns[2], ns[1]
            elif ns[1][1] == ns[2][1]:
                ns[0], ns[2] = ns[2], ns[0]
            bi_add_edge(ns[0], ns[2], 1002, [y, x])
            bi_add_edge(ns[1], ns[2], 1002, [y, x])
            bi_add_edge(ns[0], ns[1], 2, [y, x])

        elif len(ns) == 4:
            for n in ns:
                G.add_edge(f"{n[0]},{n[1]}", f"{y},{x}", weight=1)
            ns.sort(key=lambda x: x[0])
            if ns[0][0] != ns[1][0]:
                ns[0], ns[2] = ns[2], ns[0]
            bi_add_edge(ns[0], ns[2], 1002, [y, x])
            bi_add_edge(ns[0], ns[3], 1002, [y, x])
            bi_add_edge(ns[1], ns[2], 1002, [y, x])
            bi_add_edge(ns[1], ns[3], 1002, [y, x])
            bi_add_edge(ns[0], ns[1], 2, [y, x])
            bi_add_edge(ns[2], ns[3], 2, [y, x])

for pos in dirs:
    if M[tuple(startpos + pos)] == ".":
        G.add_edge(
            start,
            f"{(startpos + pos)[0]},{(startpos + pos)[1]}",
            weight=1001 if pos[0] != 0 else 1,
        )

print(nx.shortest_path_length(G, source=start, target=end, weight="weight"))

result_set = set()
for path in nx.all_shortest_paths(G, source=start, target=end, weight="weight"):
    for a, b in zip(path[:-1], path[1:]):
        result_set.add(a)
        if "miss" in G.get_edge_data(a, b):
            result_set.add(G.get_edge_data(a, b)["miss"])
    result_set.add(path[-1])
print(len(result_set))
