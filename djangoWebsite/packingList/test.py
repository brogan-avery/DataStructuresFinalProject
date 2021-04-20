import unittest
from djangoWebsite.packingList.sort import Sort
from djangoWebsite.packingList.node import Node
from djangoWebsite.packingList.priorityQueue import PriorityQueue

# because of issues with Django testing, I had to recreate the models as normal classes here as mock objects to test on the data structures
class Item():
    def __init__(self, itemId = 0, item = "Item", size = "Size", price = 0, priority = 0):
        self.itemId = itemId
        self.item = item
        self.size = size
        self.price = price
        self.priority = priority

class List():
    def __init__(self, listId = 0, budget = 0):
        self.listId = listId
        self.budget = budget

# TESTING #
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.itemObj = Item(1,"test item", "small", 10.00, 1)
        self.itemObj2 = Item(2, "test item 2", "small", 15.00, 1)
        self.itemObj3 = Item(3, "test item 3", "small", 20.00, 3)
        self.itemObj4 = Item(4, "test item 4", "small", 30.00, 2)
        self.listObj = List(1,1000)

    def tearDown(self):
        del self.itemObj
        del self.itemObj2
        del self.itemObj3
        del self.itemObj4
        del self.listObj

    # tests that the object was created properly
    def testItemObjectCreation(self):
        self.assertEqual(self.itemObj.itemId, 1)
        self.assertEqual(self.itemObj.item, "test item")
        self.assertEqual(self.itemObj.size, "small")
        self.assertEqual(self.itemObj.price, 10.00)
        self.assertEqual(self.itemObj.priority, 1)

    # tests that the object was created properly
    def testListObjectCreation(self):
        self.assertEqual(self.listObj.listId,1)
        self.assertEqual(self.listObj.budget, 1000)

    # tests the creation of a node object from item object
    def testCreateNode(self):
        testNode = Node(self.itemObj.itemId,self.itemObj.priority)
        self.assertEqual(testNode.id, 1)
        self.assertEqual(testNode.priorityLevel, 1)

    # tests the priority queue - enqueue
    def testEnqueueItem(self):
        testQueue = PriorityQueue()
        node1 = Node(1,1)
        node2 = Node(2, 1)
        node3 = Node(3, 3)
        node4 = Node(4, 2)
        testQueue.enqueue(node1.id, node1.priorityLevel)
        testQueue.enqueue(node2.id, node2.priorityLevel)
        testQueue.enqueue(node3.id, node3.priorityLevel)
        testQueue.enqueue(node4.id, node4.priorityLevel)
        self.assertEqual(testQueue.items[0].id, node1.id)
        self.assertEqual(testQueue.items[1].id, node2.id)
        self.assertEqual(testQueue.items[2].id, node4.id)
        self.assertEqual(testQueue.items[3].id, node3.id)

    # tests the priority queue - dequeue
    def testDequeueItem(self):
        testQueue = PriorityQueue()
        node1 = Node(1, 1)
        node2 = Node(2, 1)
        testQueue.enqueue(node1.id, node1.priorityLevel)
        testQueue.enqueue(node2.id, node2.priorityLevel)
        testQueue.dequeue()
        self.assertEqual(testQueue.dequeue().id, node2.id)

    # test the insertion sort from the sort class
    def testInsertionSort(self):
        testArray = [0] * 4
        testArray[0] = self.itemObj
        testArray[1] = self.itemObj2
        testArray[2] = self.itemObj3
        testArray[3] = self.itemObj4
        testSortObj = Sort(testArray)
        testSortObj.insertionSort()
        self.assertEqual(testSortObj.arr, testArray)

if __name__ == '__main__':
    unittest.main()
