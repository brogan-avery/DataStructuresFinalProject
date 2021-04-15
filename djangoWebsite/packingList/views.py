from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, List
from datetime import date, timedelta
import requests
import json
from django.http import HttpResponseRedirect
from .priorityQueue import PriorityQueue


def index(request):
    template = "packingList/index.html"
    rows = Item.objects.all()
    budget = List.objects.get(pk=1)
    freeRows = Item.objects.filter(price = 0)


    totalPrice = 0
    for row in rows:
        totalPrice = totalPrice + row.price



    priorityQueueOfItems = PriorityQueue()

    for row in rows:
        priorityQueueOfItems.enqueue(row.pk, row.priority)

    queueItems = priorityQueueOfItems.items   #[3].id

    priorityRows = []
    for i in range(queueItems.__len__()):
        row = Item.objects.get(pk=queueItems[i].id)
        priorityRows.append(row )
        if i == 9:
            break

    totalPriceForPriorityItems = 0
    for row in priorityRows:
        totalPriceForPriorityItems = totalPriceForPriorityItems + row.price

    budgetAfterPriorityItems = budget.budget - totalPriceForPriorityItems



    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key.price < arr[j].price:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    numRows = 0
    for row in rows:
        numRows = numRows + 1

    rowsByPrice = [0] * numRows

    for i in range(rowsByPrice.__len__()):
        rowsByPrice[i] = rows[i]

    insertion_sort(rowsByPrice) # sort the list of prices

    sortBy = "id"
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList:  # if the list exists
        sortBy = inputValuesList[1]


    # display by ID or price
    if sortBy == "price":
        rowsToDisplay = rowsByPrice
    else:
        rowsToDisplay = rows




    return render(request,template, {"rows" : rows, "freeRows" : freeRows, "budget" : budget.budget, "totalPrice" : totalPrice, "queueItems" : queueItems, "priorityRows" : priorityRows, "totalPriceForPriorityItems" : totalPriceForPriorityItems, "budgetAfterPriorityItems" : budgetAfterPriorityItems, "rowsToDisplay" : rowsToDisplay })





def updateBudget(request):
    template = "packingList/updateBudget.html"
    budget = List.objects.get(pk=1)
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList:
        newBudget = inputValuesList[1]
    else:
        newBudget = budget.budget
    budget.budget = newBudget
    budget.save()
    return render(request, template, {"budget" : budget.budget, "newBudget" : newBudget})

def editList(request):
    template = "packingList/editList.html"
    rows = Item.objects.all()
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList: # if the list exists
        if inputValuesList.__len__() == 5: # add new entry to list
            item = inputValuesList[1]
            size = inputValuesList[2]
            price = inputValuesList[3]
            priority = inputValuesList[4]
            newEntry = Item(item=item, size=size, price=price, priority=priority)
            newEntry.save()
        if inputValuesList.__len__() == 6:  # edit an entry on the list
            itemid = inputValuesList[1]
            item = inputValuesList[2]
            size = inputValuesList[3]
            price = inputValuesList[4]
            priority = inputValuesList[5]
            itemToEdit = Item.objects.get(pk=itemid)
            itemToEdit.item = item
            itemToEdit.size = size
            itemToEdit.price = price
            itemToEdit.priority = priority
            itemToEdit.save()
        if inputValuesList.__len__() == 2:  # to delete an entry on the list
            itemid = inputValuesList[1]
            objToDelete = Item.objects.get(pk=itemid)
            objToDelete.delete()

    return render(request, template, {"rows" : rows, "inputValuesList" : inputValuesList})
