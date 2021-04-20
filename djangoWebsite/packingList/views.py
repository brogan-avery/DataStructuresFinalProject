from django.shortcuts import render
from .models import Item, List
from .priorityQueue import PriorityQueue
from .sort import Sort
# there may be a few things in here that are not 100% necessary for the scope of this class, but I added them in there be cause a will add to it after the end of this project scope.

def index(request):
    template = "packingList/index.html" # tells this view file what HTML file to connect to in the templates folder
    rows = Item.objects.all() # all rows of data (or objects and attributes) from a table
    budget = List.objects.get(pk=1)
    freeRows = Item.objects.filter(price = 0) # get the rows where the price is 0

    # get total cost of all items
    totalPrice = 0
    for row in rows:
        totalPrice = totalPrice + row.price

    # put the items into a PQ
    priorityQueueOfItems = PriorityQueue()
    for row in rows:
        priorityQueueOfItems.enqueue(row.pk, row.priority)
    queueItems = priorityQueueOfItems.items

    # store the top 10 priority items to a list
    priorityRows = []
    for i in range(queueItems.__len__()):
        row = Item.objects.get(pk=queueItems[i].id)
        priorityRows.append(row )
        if i == 9:
            break

    # get the total cost of just the priority items
    totalPriceForPriorityItems = 0
    for row in priorityRows:
        totalPriceForPriorityItems = totalPriceForPriorityItems + row.price

    # the remain budget or overage if the user was to buy all 10 priority items
    budgetAfterPriorityItems = budget.budget - totalPriceForPriorityItems


    # sort items by price
    numRows = 0
    for row in rows:
        numRows = numRows + 1
    rowsByPrice = [0] * numRows
    for i in range(rowsByPrice.__len__()):
        rowsByPrice[i] = rows[i]
    sortObject = Sort(rowsByPrice)  # calls sort method from class
    sortObject.insertionSort() # sort the list of prices
    rowsByPrice = sortObject.arr

    sortBy = "id" # default is to sort by ID

    # gets the users input from the radio buttons to sort by price or ID
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

# this page is used to change the budget
def updateBudget(request):
    template = "packingList/updateBudget.html"
    budget = List.objects.get(pk=1)

    # gets user input for new budget value
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList: # if the list exists
        newBudget = inputValuesList[1] # updates budget to new
    else:
        newBudget = budget.budget # sets budget value to what it already was
    budget.budget = newBudget
    budget.save() # saves the changes made to the object in the database table

    return render(request, template, {"budget" : budget.budget, "newBudget" : newBudget})

# this page is used to change the items on the list
def editList(request):
    template = "packingList/editList.html"
    rows = Item.objects.all()

    # gets the form input
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    # knows which form has been submitted by how many user input values were sent in the list
    if inputValuesList: # if the list exists
        if inputValuesList.__len__() == 5: # add new entry to list
            item = inputValuesList[1]
            size = inputValuesList[2]
            price = inputValuesList[3]
            priority = inputValuesList[4]
            newEntry = Item(item=item, size=size, price=price, priority=priority) # creates a new object
            newEntry.save() # saves the new object
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
            itemToEdit.save() # saves the changes made to an existing object
        if inputValuesList.__len__() == 2:  # to delete an entry on the list
            itemid = inputValuesList[1]
            objToDelete = Item.objects.get(pk=itemid)
            objToDelete.delete()

    return render(request, template, {"rows" : rows, "inputValuesList" : inputValuesList})
