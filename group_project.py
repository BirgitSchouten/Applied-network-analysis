import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

with open('nodelist.csv', 'r') as nodefile:
    next(nodefile) # skip first line with headers
    for line in nodefile:
        id, role, community = line.split(',')
        graph.add_node(id, role = role, community = community)

with open('edgelist-early.csv', 'r') as edgefile:
    next(edgefile)
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph.add_edge(node1, node2, weight = weight)

nx.draw(graph)
plt.savefig('graph.png')