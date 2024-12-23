import networkx as nx
import itertools

G = nx.Graph()

tnodes = []
data = open("day23input.txt").read().split("\n")
for line in data:
    a, b = line.split("-")
    G.add_edge(a, b)

combos = set()
for clique in nx.find_cliques(G):
    for combo in itertools.combinations(clique, 3):
        if len(list(filter(lambda x: x[0] == "t", combo))):
            combos.add(tuple(sorted(combo)))
print(len(combos))
