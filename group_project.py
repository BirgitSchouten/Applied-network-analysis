import networkx as nx
import matplotlib.pyplot as plt

graph_early = nx.DiGraph()
graph_middle = nx.DiGraph()
graph_late = nx.DiGraph()

with open('nodelist.csv', 'r') as nodefile:
    next(nodefile) # skip first line with headers
    for line in nodefile:
        id, role, community = line.split(',')
        graph_early.add_node(id, role = role, community = community)
        graph_middle.add_node(id, role = role, community = community)
        graph_late.add_node(id, role = role, community = community)

with open('edgelist-early.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_early.add_edge(node1, node2, weight = weight)

with open('edgelist-middle.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_middle.add_edge(node1, node2, weight = weight)

with open('edgelist-late.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_late.add_edge(node1, node2, weight = weight)

get_community = nx.get_node_attributes(graph_early, 'community')
node_colors = []
for node in graph_early:
    print(node, get_community[node])
    if get_community[node] == 'Professional':
        node_colors.append('red')
    elif get_community[node] == "Personal":
        node_colors.append('blue')
    else:
        node_colors.append('purle')
print(node_colors)

nx.draw_networkx(graph_early, pos=nx.spring_layout(graph_early), with_labels = False, node_size = 100)
plt.savefig('graph_early.png')