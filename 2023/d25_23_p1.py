import networkx as nx
dat = [[line.split(':')[0], line.split(':')[1].split()]  for line in open('d25_23.txt').read().splitlines()]

graph = nx.Graph()

for node, nhbrs in dat:
    for nhb in nhbrs:
        graph.add_edge(node, nhb)
        graph.add_edge(nhb, node)

# find the minimum edges that cut the graph
cut_edges = nx.minimum_edge_cut(graph)
assert len(cut_edges) == 3

# remove those from the graph
graph.remove_edges_from(cut_edges)

# get the connected components of the graph
connected_components = list(nx.connected_components(graph))
assert len(connected_components) == 2

# find the product of the len of each of the two connected component
print(len(connected_components[0])*len(connected_components[1]) )