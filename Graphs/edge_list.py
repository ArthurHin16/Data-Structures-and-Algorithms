import networkx as nx
import matplotlib.pyplot as plt

# Define the edge list
edge_list = [(1, 2), (2, 3), (3, 1)]

# Create a graph object
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edge_list)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
plt.show()
