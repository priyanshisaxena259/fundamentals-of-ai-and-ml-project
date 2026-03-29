import networkx as nx
import matplotlib.pyplot as plt
from graph_data import graph

def visualize_graph(path=None):
    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=3)

    plt.title("Smart Route Finder (A*)")
    plt.show()