# import unittest
# from nose.tools import assert_true
# from unittest.mock import patch
# import requests
# from diet.models import Food_items, Consumption
#
# class MyTestCase(unittest.TestCase):
#     # setting up a test object for the classes in the .models file
#     def setUp(self):
#         self.consumptionEntry = Consumption(item='grapes', cals=62, date='2020-12-01')
#         self.foodItemEntry = Food_items(item='grapes', cals=62, group='fruit')
#
#     def tearDown(self):
#         del self.consumptionEntry
#         del self.foodItemEntry
#
#     def test_consumption_entry_creation(self):
#         self.assertEqual(self.consumptionEntry.item, "grapes")
#         self.assertEqual(self.consumptionEntry.cals, 62)
#         self.assertEqual(self.consumptionEntry.date, "2020-12-01")
#
#     def test_food_items_entry_creation(self):
#         self.assertEqual(self.foodItemEntry.item, "grapes")
#         self.assertEqual(self.foodItemEntry.cals, 62)
#         self.assertEqual(self.foodItemEntry.group, "fruit")
#
#
#
# if __name__ == '__main__':
#     unittest.main()
