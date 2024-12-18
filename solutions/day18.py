import networkx as nx

field_size = 6
bytes_limit = 12

G = nx.complete_graph((field_size + 1) ** 2)

data = open("day18example.txt").read().split("\n")
for line in data:
    x, y = map(int, line.split(","))
    print(x, y)
    G.remove_node(x + y * (field_size + 1))

print(nx.shortest_path_length(G, 0, (field_size + 1) ** 2 - 1))
