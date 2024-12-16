import numpy as np
import networkx as nx

M = np.genfromtxt("day16input.txt", dtype=str, comments="_", delimiter=1)
G = nx.DiGraph()
dirs = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

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
                G.add_edge(
                    f"{ns[0][0]},{ns[0][1]}",
                    f"{ns[1][0]},{ns[1][1]}",
                    weight=1002,
                )
                G.add_edge(
                    f"{ns[1][0]},{ns[1][1]}",
                    f"{ns[0][0]},{ns[0][1]}",
                    weight=1002,
                )

        elif len(ns) == 3:
            for n in ns:
                G.add_edge(f"{n[0]},{n[1]}", f"{y},{x}", weight=1)

            if ns[0][0] == ns[2][0]:
                tmp = ns[1]
                ns[1] = ns[2]
                ns[2] = tmp
            elif ns[1][0] == ns[2][0]:
                tmp = ns[0]
                ns[0] = ns[2]
                ns[2] = tmp
            elif ns[0][1] == ns[2][1]:
                tmp = ns[1]
                ns[1] = ns[2]
                ns[2] = tmp
            elif ns[1][1] == ns[2][1]:
                tmp = ns[0]
                ns[0] = ns[2]
                ns[2] = tmp

            G.add_edge(f"{ns[0][0]},{ns[0][1]}", f"{ns[2][0]},{ns[2][1]}", weight=1002)
            G.add_edge(f"{ns[2][0]},{ns[2][1]}", f"{ns[0][0]},{ns[0][1]}", weight=1002)
            G.add_edge(f"{ns[1][0]},{ns[1][1]}", f"{ns[2][0]},{ns[2][1]}", weight=1002)
            G.add_edge(f"{ns[2][0]},{ns[2][1]}", f"{ns[1][0]},{ns[1][1]}", weight=1002)
            G.add_edge(f"{ns[0][0]},{ns[0][1]}", f"{ns[1][0]},{ns[1][1]}", weight=2)
            G.add_edge(f"{ns[1][0]},{ns[1][1]}", f"{ns[0][0]},{ns[0][1]}", weight=2)

        elif len(ns) == 4:
            for n in ns:
                G.add_edge(f"{n[0]},{n[1]}", f"{y},{x}", weight=1)

            ns.sort(key=lambda x: x[0])
            if ns[0][0] != ns[1][0]:
                tmp = ns[0]
                ns[0] = ns[2]
                ns[2] = tmp

            G.add_edge(f"{ns[0][0]},{ns[0][1]}", f"{ns[2][0]},{ns[2][1]}", weight=1002)
            G.add_edge(f"{ns[2][0]},{ns[2][1]}", f"{ns[0][0]},{ns[0][1]}", weight=1002)
            G.add_edge(f"{ns[0][0]},{ns[0][1]}", f"{ns[3][0]},{ns[3][1]}", weight=1002)
            G.add_edge(f"{ns[3][0]},{ns[3][1]}", f"{ns[0][0]},{ns[0][1]}", weight=1002)

            G.add_edge(f"{ns[1][0]},{ns[1][1]}", f"{ns[2][0]},{ns[2][1]}", weight=1002)
            G.add_edge(f"{ns[2][0]},{ns[2][1]}", f"{ns[1][0]},{ns[1][1]}", weight=1002)
            G.add_edge(f"{ns[1][0]},{ns[1][1]}", f"{ns[3][0]},{ns[3][1]}", weight=1002)
            G.add_edge(f"{ns[3][0]},{ns[3][1]}", f"{ns[1][0]},{ns[1][1]}", weight=1002)

            G.add_edge(f"{ns[0][0]},{ns[0][1]}", f"{ns[1][0]},{ns[1][1]}", weight=2)
            G.add_edge(f"{ns[1][0]},{ns[1][1]}", f"{ns[0][0]},{ns[0][1]}", weight=2)
            G.add_edge(f"{ns[2][0]},{ns[2][1]}", f"{ns[3][0]},{ns[3][1]}", weight=2)
            G.add_edge(f"{ns[3][0]},{ns[3][1]}", f"{ns[2][0]},{ns[2][1]}", weight=2)

for pos in dirs:
    if M[tuple(startpos + pos)] == ".":
        G.add_edge(
            start,
            f"{(startpos + pos)[0]},{(startpos + pos)[1]}",
            weight=1001 if pos[0] != 0 else 1,
        )

print(nx.shortest_path_length(G, source=start, target=end, weight="weight"))
