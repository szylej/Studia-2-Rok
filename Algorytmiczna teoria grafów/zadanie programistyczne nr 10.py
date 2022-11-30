import networkx as nx
import matplotlib.pyplot as plt
H1 = [0, 1, 2, 3, 4, 5]

G = nx.Graph()
G.add_nodes_from(H1)
G.add_edge(0, 1)
G.add_edge(0, 4)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.remove_node(0)
G.remove_node(4)
print(G.nodes())
print(G.edges())
H = nx.Graph(G)
nx.draw(H, node_size=2)
plt.show()
