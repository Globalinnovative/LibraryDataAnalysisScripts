#!/usr/bin/env python3
# coding: utf-8

"The scipt that handles csv input."
import csv2Graph
import matplotlib.pyplot as plt
import networkx as nx


if __name__ == "__main__":
    csvobj = csv2Graph.csv2Graph("data/libsample.csv")
    nodes = csvobj.createNodeList(7)
    relation = csvobj.createNodeList(1)
    edges = csvobj.createEdgeList(nodes, {1: relation})
    graph = csvobj.createGraph(nodes, edges)
    nx.draw(graph)
    nx.write_graphml(graph, "test.graphml")
    print("Number of edges in graph: ", graph.number_of_edges())
    plt.show()
