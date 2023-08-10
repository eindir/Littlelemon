from django.test import TestCase
from ..models import Menu

#TestCase class
class MenuViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        #setup dtata for all tests cases
        cls.item1 = Menu.objects.create(Title="Ice Cream", Price=3, Inventory=100)
        cls.item2 = Menu.objects.create(Title="Cheesecake", Price=12, Inventory=15)
    
    def test_get_item(self):
        self.assertEqual(str(MenuViewTest.item1), "Ice Cream : 3")
        self.assertEqual(str(MenuViewTest.item2), "Cheesecake : 12")