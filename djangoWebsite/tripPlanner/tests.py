# from django.test import TestCase
# from django.test import Client
# import unittest
# from nose.tools import assert_true
# from diet import views
# from datetime import date
# from .views import *
#
# class MyTestCase(TestCase):
#     # setting up a test object for the classes in the .models file
#     def setUp(self):
#         self.consumptionEntry = Consumption.objects.create(item='grapes', cals=62, date='2020-12-01')
#         self.foodItemEntry = Food_items.objects.create(item='grapes', cals=62, group='fruit')
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
#     #makes sure that a connection can be made with the api
#     def test_api_connection(self):
#         url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
#         querystring = {"query": 'grapes'}
#         headers = {
#             'x-rapidapi-key': "0656d65008msh3c3913809c5f6b7p1b6e80jsn1ac0d096c06a",
#             'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
#         }
#         response = requests.request("GET", url, headers=headers, params=querystring)
#         assert_true(response.ok)
#
#
#
# if __name__ == '__main__':
#     unittest.main()