"""
***************************************************************
* Class Name: Graph
* Author: Brogan Avery
* Created: 2021-03-25
***************************************************************
"""

class Graph:
    def __init__(self, numNodes):
        self.numNodes = numNodes # number of nodes on the graph
        self.graph = [] # empty list to store lists that contain 2 nodes and an edge

    def add_edge(self, nodeA, nodeB, edgeBetween): # an edge can also be like a row of a graph/dict
        self.graph.append([nodeA, nodeB, edgeBetween]) # add a list that represents node A, Node B, and the distance or weight between

    def find(self, nodeCountList, i):
        if nodeCountList[i] == i:
            return i
        return self.find(nodeCountList, nodeCountList[i])

    def apply_union(self, nodeCountList, rank, x, y): # adds parents to children
        xroot = self.find(nodeCountList, x)
        yroot = self.find(nodeCountList, y)
        if rank[xroot] < rank[yroot]:
            nodeCountList[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            nodeCountList[yroot] = xroot
        else:
            nodeCountList[yroot] = xroot
            rank[xroot] += 1



