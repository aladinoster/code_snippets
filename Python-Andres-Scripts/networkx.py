from networkx import DiGraph
import networkx as nx
import matplotlib.pyplot as plt

G = DiGraph()

G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edges_from([(1, 2), (1, 3)])
H = nx.path_graph(10)
G.add_nodes_from(H)

nx.draw(G)

plt.show()
