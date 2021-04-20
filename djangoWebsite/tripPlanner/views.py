from django.shortcuts import render
from .models import Location
from math import radians, cos, sin, asin, sqrt,trunc
from .Graph import Graph
from .MatrixGraph import MatrixGraph

# there may be a few things in here that are not 100% necessary for the scope of this class, but I added them in there be cause a will add to it after the end of this project scope.

def index(request):
    template = "tripPlanner/index.html" # tells this view file what HTML file to connect to in the templates folder
    rows = Location.objects.all() # all rows of data (or objects and attributes) from a table

    return render(request, template, {"rows": rows})

# this page edits locations on the list
def editList(request):
    template = "tripPlanner/editList.html"
    rows = Location.objects.all()

    # gets user input from form
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList:  # if the list exists
        if inputValuesList.__len__() == 5:  # add new entry to list
            location = inputValuesList[1]
            state = inputValuesList[2]
            lat = inputValuesList[3]
            lon = inputValuesList[4]
            newEntry = Location(location=location, state=state, lat=lat, lon=lon)
            newEntry.save()
        if inputValuesList.__len__() == 6:  # edit an entry on the list
            locationid = inputValuesList[1]
            location = inputValuesList[2]
            state = inputValuesList[3]
            lat = inputValuesList[4]
            lon = inputValuesList[5]
            locationToEdit = Location.objects.get(pk=locationid)
            locationToEdit.location = location
            locationToEdit.state = state
            locationToEdit.lat = lat
            locationToEdit.lon = lon
            locationToEdit.save()
        if inputValuesList.__len__() == 2:  # to delete an entry on the list
            locationid = inputValuesList[1]
            objToDelete = Location.objects.get(pk=locationid)
            objToDelete.delete()

    return render(request, template, {"rows": rows, "inputValuesList": inputValuesList})

# used to query the graph to find distance between 2 locations
def buildTrip(request):
    template = "tripPlanner/buildTrip.html"  # tells this view file what HTML file to connect to in the templates folder
    rows = Location.objects.all()  # all rows of data (or objects and attributes) from a table

    # most of this math formula came from https: // www.geeksforgeeks.org / program - distance - two - points - earth /
    def distance(lat1, lon1, lat2, lon2):  # inner function to calculate distance between two coord. sets. Needed for Django friendly set up
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 3956  # earth radius
        ans = c * r
        ans = trunc(ans)
        return (ans)

    objIDs = []  # list of all the PKs/IDs currently on the locations table EX. [1,2,3,6,7,8,9,10,12] (some objects may get deleted)
    matrixOfIDs = []  # creates something like a matrix of the pks, All nodes are connected to every node directly ( Each PK in the list has its own list of PKs )

    for row in rows:
        objIDs.append(row.pk)  # populates ID list

    for id in objIDs:  # creates nested lists
        matrixOfIDs.append([[id], objIDs])  # populates matrix of IDs

    graph = Graph(objIDs.__len__())  # creates a normal graph

    matrixOfDistances = []  # replaces the pk values in the ID matrix with the objs corresponding distances from each node to each node

    for each in matrixOfIDs:  # gets all the miles between each place
        matrixRow = []  # each row in matrix
        for i in range(matrixOfIDs.__len__()):  # gets the lon and lat of the two "nodes" being compared
            loc1 = Location.objects.get(pk=each[0][0])
            loc2 = Location.objects.get(pk=each[1][i])
            lat1 = loc1.lat
            lon1 = loc1.lon
            lat2 = loc2.lat
            lon2 = loc2.lon
            result = distance(lat1, lon1, lat2, lon2) # calls method to do earth math
            matrixRow.append(result)  # the edge/ miles between two nodes
            graph.add_edge(loc1, loc2, result)  # adds edges to the normal graph
        matrixOfDistances.append(matrixRow)  # adds each row of miles to a matrix

    matrixGraph = MatrixGraph(objIDs.__len__())  # creates a new Matrix Graph object with the number of nodes = number of Location table objects
    matrixGraph.graph = matrixOfDistances  # sets the distance matrix as the graph value for object

    # gets user input from form for a start and and end location
    distanceBetween = 0
    location1id = 0
    location2id = 0
    inputSelection = request.POST
    inputDict = inputSelection.dict()
    inputValuesList = list(inputDict.values())
    if inputValuesList:  # if the list exists, store the loc1 and loc2 ID from the form
        location1id = inputValuesList[1]
        location2id = inputValuesList[2]

    # matches the user request to an edge in the graph and gets the miles between
    for i in range(graph.graph.__len__()):
        if str(graph.graph[i][0].pk) == str(location1id):
            if str(graph.graph[i][1].pk) == str(location2id):
                distanceBetween = graph.graph[i][2]

    return render(request, template, {"rows": rows, "result": result, "objIDs": objIDs, "matrixOfIDs": matrixOfIDs, "matrixOfDistances": matrixOfDistances, "graph": graph.graph, "distanceBetween" : distanceBetween})
