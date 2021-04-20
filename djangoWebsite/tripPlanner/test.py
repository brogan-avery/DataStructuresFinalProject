import unittest
from djangoWebsite.tripPlanner.Graph import Graph

# because of issues with Django testing, I had to recreate the models as normal classes here as mock objects to test on the data structures
class Location():
    def __init__(self, locationId = 0, location = " ", lat = 0, lon = 0, state = " "):
        self.locationId = locationId
        self.location = location
        self.lat = lat
        self.lon = lon
        self.state = state

# TESTING #
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.locationObj = Location(1, "test location", 100.55, 200.66, "Iowa" )
        self.locationObj2 = Location(2, "test location 2", 10.989, 260.983, "Texas")
        self.locationObj3 = Location(3, "test location 3", 90.85, 140.626, "Utah")

    def tearDown(self):
        del self.locationObj
        del self.locationObj2
        del self.locationObj3

    # tests that the object was created properly
    def testLocationObjectCreation(self):
        self.assertEqual(self.locationObj.locationId, 1)
        self.assertEqual(self.locationObj.location, "test location")
        self.assertEqual(self.locationObj.lat, 100.55)
        self.assertEqual(self.locationObj.lon, 200.66)
        self.assertEqual(self.locationObj.state, "Iowa")

    # tests the creation of Graph object from nodes locations and distances and adding in the eddges
    def testGraphAddEdges(self):
        testGraph = Graph(3)
        testGraph.add_edge(self.locationObj,self.locationObj2, 100)
        testGraph.add_edge(self.locationObj, self.locationObj3, 500)
        testGraph.add_edge(self.locationObj2, self.locationObj3, 900)
        self.assertEqual(testGraph.graph, [[self.locationObj,self.locationObj2, 100],[self.locationObj, self.locationObj3, 500],[self.locationObj2, self.locationObj3, 900]])

if __name__ == '__main__':
    unittest.main()
