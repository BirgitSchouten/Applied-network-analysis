import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

# read csv file and create network
with open('output/nodelist.csv', 'r') as nodefile:
    next(nodefile) # skip header line
    for line in nodefile:
        id, ecli, subject, subtopic = line.split(",")
        graph.add_node(id, ecli = ecli.strip(), subject = subject.strip(), subtopic = subtopic.strip())
    
with open('output/edgelist.csv', 'r') as edgefile:
    next(edgefile)
    for line in edgefile:
        node1, node2 = line.strip().split(",")
        graph.add_edge(node1, node2)

# remove isolates for visualisation
isolates = list(nx.isolates(graph))
graph.remove_nodes_from(isolates)

# define coloring of nodes in visualisation based on the subject
node_colors = []
for n, data in graph.nodes(data = True):
    if data['subject'] == "Bestuursrecht":
        node_colors.append("#12355B")
    elif data['subject'] == "Civiel recht":
        node_colors.append("#420039")
    elif data['subject'] == "Strafrecht":
        node_colors.append("#D72638")
    elif data['subject'] == "Internationaal publiekrecht":
        node_colors.append("#FF570A")

# # visualise graph
# fig, (ax0, ax1) = plt.subplots(nrows = 1,
#                                 ncols = 2)

position = nx.spring_layout(graph, seed = 60)
nx.draw_networkx(graph, pos = position,
                 with_labels = False,
                 node_size = 10,
                 node_color = node_colors)

plt.savefig('network.png')