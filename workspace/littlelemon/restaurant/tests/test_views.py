from django.test import TestCase
from restaurant.models import *

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Bananas", Price=2, Inventory=24)
        Menu.objects.create(Title="Pears", Price=3, Inventory=10)
        Menu.objects.create(Title="Apples", Price=2.75, Inventory=50)
    def test_getall(self):
        item1 = Menu.objects.get(Title="Bananas")
        item2 = Menu.objects.get(Title="Pears")
        item3 = Menu.objects.get(Title="Apples")
        self.assertEqual(str(item1), "Bananas : 2.00")
        self.assertEqual(str(item2), "Pears : 3.00")
        self.assertEqual(str(item3), "Apples : 2.75")
        
        