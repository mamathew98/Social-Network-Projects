# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def q1(n, c):
    G = nx.watts_strogatz_graph(n, 2 * c, 0)
    return G


# for i in range(2, 51):
#     g = q1(200, i)
#     print("CC(", i, "): ", nx.clustering(g, 0))
#     print("avg: ", nx.average_shortest_path_length(g))


n =10
c = 2
test = q1(n, c)
# nx.draw(test, with_labels=True)
print("CC1(", c, "): ", nx.average_shortest_path_length(test))
test.remove_edge(1, 3)
test.add_edge(1, 6)
nx.draw(test, with_labels=True)
print("CC2(", c, "): ", nx.average_shortest_path_length(test))
plt.show()


# G = nx.Graph()
# G.add_nodes_from([
#     (1, {"color": "black"}),
#     (2, {"color": "black"}),
#     (3, {"color": "black"}),
#     (4, {"color": "blue"}),
#     (5, {"color": "blue"}),
#     (6, {"color": "red"}),
#     (7, {"color": "red"}),
#     (8, {"color": "green"}),
#     (9, {"color": "green"}),
# ])
#
#
# G.add_edge(1, 2, color='black')
# G.add_edge(1, 3, color='black')
# G.add_edge(1, 4, color='black')
# G.add_edge(1, 5, color='black')
# G.add_edge(1, 6, color='black')
# G.add_edge(1, 7, color='black')
# G.add_edge(1, 8, color='black')
# G.add_edge(1, 9, color='black')
# G.add_edge(2, 3, color='blue')
# G.add_edge(2, 4, color='blue')
# G.add_edge(3, 5, color='blue')
#
# G.add_edge(2, 5, color='red')
# G.add_edge(3, 4, color='red')
# G.add_edge(4, 6, color='red')
# G.add_edge(5, 7, color='red')
# G.add_edge(2, 7, color='red')
# G.add_edge(3, 7, color='red')
# G.add_edge(2, 6, color='red')
#
# G.add_edge(6, 8, color='green')
# G.add_edge(7, 9, color='green')
# G.add_edge(3, 9, color='green')
# G.add_edge(5, 9, color='green')
# G.add_edge(2, 8, color='green')
# G.add_edge(4, 8, color='green')
# G.add_edge(2, 7, color='green')
# G.add_edge(4, 5, color='green')
# G.add_edge(3, 6, color='green')
#
#
# colors = nx.get_edge_attributes(G, 'color').values()
#
# pos = nx.circular_layout(G)
#
# nx.draw(G, pos,
#         edge_color=colors,
#         with_labels=True,
#         node_color='lightgreen')
# plt.show()
