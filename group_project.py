import networkx as nx
import matplotlib.pyplot as plt

graph_early = nx.DiGraph()
graph_middle = nx.DiGraph()
graph_late = nx.DiGraph()

# read csv files and create 3 networks
with open('nodelist.csv', 'r') as nodefile:
    next(nodefile) # skip first line with headers
    for line in nodefile:
        id, role, community = line.split(',')
        graph_early.add_node(id, role = role, community = community.strip())
        graph_middle.add_node(id, role = role, community = community.strip())
        graph_late.add_node(id, role = role, community = community.strip())

with open('edgelist-early.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_early.add_edge(node1, node2, weight = int(weight.strip()))

with open('edgelist-middle.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_middle.add_edge(node1, node2, weight = int(weight.strip()))

with open('edgelist-late.csv', 'r') as edgefile:
    next(edgefile) # skip headers
    for line in edgefile:
        node1, node2, weight = line.split(',')
        graph_late.add_edge(node1, node2, weight = int(weight.strip()))

# remove unconnected nodes per week? ONLY FOR VISUALISATION
isolates_early = list(nx.isolates(graph_early))
isolates_middle = list(nx.isolates(graph_middle))
isolates_late = list(nx.isolates(graph_late))

# define coloring of nodes in visualisation based on the community they're placed in
node_colors = []
for n, data in graph_early.nodes(data = True):
    if data['community'] == 'Professional' or data['community'] == "Professional_I":
        node_colors.append("#ff5A5f")
    elif data['community'] == "Personal":
        node_colors.append("#087e8b")
    else:
        node_colors.append("#3c3c3c")

# define edge color based on weight
subset_color = ["#ffffff", "#c1839f", "#884463", "#361b27"]
edge_colors_early = [subset_color[data['weight']] for start, end, data in graph_early.edges(data = True)]
edge_colors_middle = [subset_color[data['weight']] for start, end, data in graph_middle.edges(data = True)]
edge_colors_late = [subset_color[data['weight']] for start, end, data in graph_late.edges(data = True)]

# visualise graphs
fig, (ax0, ax1, ax2) = plt.subplots(nrows = 1, ncols = 3, sharex = True, figsize = (24, 7))
fig.suptitle("Directed network of self-reported interations between students in biology course")

ax0.set_title('Week 6')
nx.draw_networkx(graph_early, pos=nx.spring_layout(graph_early),
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_early,
                 ax = ax0)

ax1.set_title('Week 11')
nx.draw_networkx(graph_middle, pos=nx.spring_layout(graph_middle),
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_middle,
                 ax = ax1)

ax2.set_title('Week 15')
nx.draw_networkx(graph_late, pos=nx.spring_layout(graph_late),
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_late,
                 ax = ax2)

plt.savefig('all_graps.png')