import networkx as nx
G = nx.Graph({0: [1, 2, 8, 9], 1: [0, 2, 3, 4, 9], 2: [0, 1, 3, 4, 5, 7, 8, 9],
              3: [1, 2, 7, 8, 9], 4: [1, 2], 5: [2, 6, 7], 6: [5, 8, 9],
              7: [2, 3, 5], 8: [0, 2, 3, 6, 9], 9: [0, 1, 2, 3, 6, 8]})

A = nx.to_dict_of_lists(G)
print(A.nodes())
print(A.edges())

