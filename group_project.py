import networkx as nx

graph = nx.Graph()

with open('nodelist.csv', 'r') as nodefile:
    next(nodefile) # skip first line with headers
    for line in nodefile:
        id, role, community = line.split(',')
        graph.add_node(id, role = role, community = community)

