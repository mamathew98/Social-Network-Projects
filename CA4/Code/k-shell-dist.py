import pandas as pd
import matplotlib as plt
import networkx as nx

# data = pd.read_csv("barjam_edges.csv")
# source = data["Source"]
# target = data["Target"]
#
# df = pd.DataFrame({"Source": list(data["Source"]),
#                    "Target": list(data["Target"])})
#
# df.to_csv('edges.csv', index=None)
from tqdm import tqdm

nodes = pd.read_csv("nodes.csv")

fh = open("edges.csv", "rb")
G = nx.read_edgelist(fh, delimiter=',')
fh.close()
print(len(G.edges()))

shells = []
for i in tqdm(range(10, 50)):
    shell = nx.k_shell(G, i)
    shells.append(shell.nodes)


# filtered = nodes[(nodes["Id"] in shells[-1])]
# filtered.to_csv("test.csv")
# labels = {}
for p in nodes.iterrows():
    if str(p[1]["Id"]) in shells[-2]:
        print(p[1].to_frame().T)

# df = nodes.set_index(['Id'])
# print(df.loc[df.index.isin(shells[-2])])
# print(shells.index(shells[-1]), shells[-1])
# nx.draw(shells[-1], with_labels=False)

