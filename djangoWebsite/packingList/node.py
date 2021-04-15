"""
***************************************************************
* Class Name: Node
* Author: Brogan Avery
* Created: 2021-03-05
***************************************************************
"""

class Node:
    def __init__(self, id, priorityLevel):
        self.id = id
        self.priorityLevel = priorityLevel

    def __str__(self):
        return str(self.id) + " " + str(self.priorityLevel)

