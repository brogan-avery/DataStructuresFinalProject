"""
***************************************************************
* Class Name: Matrix Graph
* Author: Brogan Avery
* Created: 2021-03-25
***************************************************************
"""

import sys

class MatrixGraph():
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.graph = [[0 for column in range(numNodes)] # initializes all index values to 0
                      for row in range(numNodes)]

    def get_min_index(self, listOfSystemLargestNums, mstSet):
        min_index = 0
        min = sys.maxsize
        for num in range(self.numNodes):
            if listOfSystemLargestNums[num] < min and mstSet[num] == False:
                min = listOfSystemLargestNums[num]
                min_index = num
        return min_index

    def prims_algo(self):
        listOfSystemLargestNums = [sys.maxsize] * self.numNodes # initializes an array the size of the number of nodes with each value containing my systems largest number
        parent = [None] * self.numNodes  # Array to store constructed MST, starts out as empty/ full of nones
        listOfSystemLargestNums[0] = 0 # Make listOfSystemLargestNums 0 so that this node is picked as first node
        mstSet = [False] * self.numNodes # initialize the list to size numNodes to all values = 'False'
        parent[0] = -1  # First node is always the root
        for i in range(self.numNodes):
            distance = self.get_min_index(listOfSystemLargestNums, mstSet) # get the minimum distance from the list of numNodes not yet checked
            mstSet[distance] = True
            for num in range(self.numNodes):  # Update dist value of the adjacent numNodes of the picked vertex only if the current distance is greater than new distance and the vertex in not in the shortest path tree
                if self.graph[distance][num] > 0 and mstSet[num] == False and listOfSystemLargestNums[num] > self.graph[distance][num]:                 # graph[distance][num] is non zero only for adjacent numNodes of mstSet[num] is false for numNodes not yet included in MST. Update the listOfSystemLargestNums only if graph[distance][num] is smaller than listOfSystemLargestNums[num]
                    listOfSystemLargestNums[num] = self.graph[distance][num]
                    parent[num] = distance
        return parent

    # this is super similar to prims
    def dijkstras_algo(self):
        listOfSystemLargestNums = [sys.maxsize] * self.numNodes # initializes an array the size of the number of nodes with each value containing my systems largest number
        listOfSystemLargestNums[0] = 0 # Make listOfSystemLargestNums 0 so that this node is picked as first node
        sptSet = [False] * self.numNodes # initialize the list to size numNodes to all values = 'False'
        for i in range(self.numNodes):
            distance = self.get_min_index(listOfSystemLargestNums, sptSet) # get the minimum distance from the list of numNodes not yet checked
            sptSet[distance] = True
            for num in range(self.numNodes): # Update dist value of the adjacent numNodes of the picked vertex only if the current distance is greater than new distance and the vertex in not in the shortest path tree
                if self.graph[distance][num] > 0 and sptSet[num] == False and listOfSystemLargestNums[num] > listOfSystemLargestNums[distance] + self.graph[distance][num]: # graph[distance][num] is non zero only for adjacent numNodes of mstSet[num] is false for numNodes not yet included in MST. Update the listOfSystemLargestNums only if graph[distance][num] is smaller than listOfSystemLargestNums[num]
                    listOfSystemLargestNums[num] = listOfSystemLargestNums[distance] + self.graph[distance][num]
        return listOfSystemLargestNums
