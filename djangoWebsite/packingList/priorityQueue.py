"""
***************************************************************
* Class Name: Priority Queue
* Author: Brogan Avery
* Created: 2021-03-05
***************************************************************
"""

from .node import Node

class PriorityQueue:
    def __init__(self):
        self.head = 0 # the next item to come out of queue
        self.tail = -1 # last item put in and last to come out
        self.size = 0 # how many memory boxes are currently in use
        self.items = [] # the queue list

    def enqueue(self, id, priorityLevel): # puts an item in the line (end of queue)
        item = Node(id, priorityLevel) # node object
        if len(self.items) == 0: # just add to end of list if queue is empty
            self.items.append(item)
        else:
            self.items.append(item) # add the new item to the end of the list to make a new space at the end to increase the list size
            # start from end of list until the new priority matches the next element to the lefts priority or until it moves all the way to the front
            i = len(self.items) - 1
            while (i >= 0):
                # gets priority level for the next item to the left to compare
                if item.priorityLevel < self.items[i].priorityLevel: # compares the two
                    self.items[i + 1] = self.items[i]
                    self.items[i] = item
                i = i - 1

    def dequeue(self):    # this is very much like the opposite of enqueue
        if not len(self.items) == 0: # in the case the queue is not empty
            item_str = self.items[self.head]
            self.items.pop(self.head)  # removes first value in the queue
            self.size -= 1   # reflects an element has been pushed through and out of the queue so the size shrinks by one
        else:
            print("Queue is empty")
        return item_str

    def print_queue(self):
        for i in self.items:
            print(i)

    def __str__(self):
        return str(self.items)