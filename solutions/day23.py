import networkx as nx
import itertools

G = nx.Graph()
data = open("day23input.txt").read().split("\n")
for line in data:
    G.add_edge(line[0:2], line[3:5])

combos = set()
max_clique = []
for clique in nx.find_cliques(G):
    if len(clique) > len(max_clique):
        max_clique = clique
    for combo in itertools.combinations(clique, 3):
        if len(list(filter(lambda x: x[0] == "t", combo))):
            combos.add(tuple(sorted(combo)))
print(len(combos))
print(",".join(sorted(max_clique)))
