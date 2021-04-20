"""
***************************************************************
* Class Name: Sort
* Author: Brogan Avery
* Created: 2021-04-10
***************************************************************
"""
class Sort():
    def __init__(self, arr):
        self.arr = arr

    # insertion sort function to sort list items by price
    def insertionSort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key.price < self.arr[j].price:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
