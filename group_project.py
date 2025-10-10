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

# # define coloring of nodes in visualisation based on the role they're given
# node_colors = []
# for n, data in graph_early.nodes(data = True):
#     if data['role'] == 'Student':
#         node_colors.append("#7FD1B9")
#     elif data['role'] == 'TA' or data['role'] == 'Instructor':
#         node_colors.append("#0E0004")
#     elif data['role'] == 'Friend':
#         node_colors.append("#D3A588")
#     elif data['role'] == 'Family member':
#         node_colors.append("#ECE2D0")
#     else:
#         node_colors.append("#084C61")

# define edge color based on weight
subset_edge_color = ["#ffffff", "#c1839f", "#884463", "#361b27"]
edge_colors_early = [subset_edge_color[data['weight']] for start, end, data in graph_early.edges(data = True)]
edge_colors_middle = [subset_edge_color[data['weight']] for start, end, data in graph_middle.edges(data = True)]
edge_colors_late = [subset_edge_color[data['weight']] for start, end, data in graph_late.edges(data = True)]

# visualise graphs
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows = 1,
                                    ncols = 4,
                                    sharex = True,
                                    figsize = (25, 7),
                                    gridspec_kw = {'width_ratios' : [4, 4, 4, 1]})
fig.suptitle("Directed network of self-reported interations between students in biology course")

# nodes legend for community
color_nodes_legend = {'Professional': "#ff5A5f",'Personal': "#087e8b",'Other': "#3c3c3c"}
for label in color_nodes_legend:
    ax3.plot([], [], 
             color = 'white',
             marker = 'o',
             markersize = 11,
             markerfacecolor = color_nodes_legend[label],
             label = label)
    
# # nodes legend for role
# color_nodes_legend = {'Student': "#7FD1B9",
#                       'TA or Instructor': "#0E0004",
#                       'Family member': "#ECE2D0",
#                       'Friend': "#D3A588",
#                       'Other': "#084C61"}
# for label in color_nodes_legend:
#     ax3.plot([], [], 
#              color = 'white',
#              marker = 'o',
#              markersize = 11,
#              markerfacecolor = color_nodes_legend[label],
#              label = label)

color_edges_legend = {'Talked once or twice': "#c1839f", 'Talked 3-4 times': "#884463", 'Talked 5-6+ times': "#361b27"}
for label in color_edges_legend:
    ax3.plot([], [],
             color = color_edges_legend[label],
             label = label)

# option to create all graphs with the same node layout
position = nx.spring_layout(graph_middle, seed = 57)

ax0.set_title('Week 6')
nx.draw_networkx(graph_early, pos = position,
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_early,
                 ax = ax0)

ax1.set_title('Week 11')
nx.draw_networkx(graph_middle, pos = position,
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_middle,
                 ax = ax1)

ax2.set_title('Week 15')
nx.draw_networkx(graph_late, pos = position,
                 with_labels = False,
                 node_size = 100,
                 node_color = node_colors,
                 edge_color = edge_colors_late,
                 ax = ax2)

ax3.axis('off')

plt.legend(frameon = False)
plt.savefig('all_graps-community-fixed_position.png')