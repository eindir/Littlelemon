from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Menu

class MenuViewSetTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        #Create some menu items for testing   
        Menu.objects.create(Title="Ice Cream", Price=3, Inventory=100)
        Menu.objects.create(Title="Cheesecake", Price=12, Inventory=15)
        Menu.objects.create(Title="Beef Wellington", Price=22, Inventory=15)

        #Get the urls for the list and detail views
        cls.item = Menu.objects.first()
        cls.list_url = reverse('menu-list')
        cls.item_url = reverse('menu-item', kwargs={'pk': cls.item.id})

    def test_getall(self):
        #Make a GET request to the list view and check the status code and the data
        response = self.client.get(MenuViewSetTestCase.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)
        
    def test_getitem(self):
        #Make a GET request to the single item view and check the status code and the data
        response = self.client.get(MenuViewSetTestCase.item_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Title"], "Ice Cream")
        self.assertEqual(response.data["Price"], "3.00")
        self.assertEqual(response.data["Inventory"], 100)
        
    """ def test_menu_create(self):
        #Make a POST request to the list view with some data and check the status code and the data
        data = {'title': 'Harry Potter and the Philosophers Stone', 'author': 'J.K. Rowling'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])

    def test_menu_retrieve(self):

        #Make a GET request to the detail view and check the status code and the data
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.book.id)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['author'], self.book.author)

    def test_menu_update(self):

        #Make a PUT request to the detail view with some data and check the status code and the data
        data = {'title': 'The Catcher in the Rye', 'author': 'John Doe'}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])

    def test_menu_partial_update(self):

        #Make a PATCH request to the detail view with some data and check the status code and the data
        data = {'author': 'Jane Doe'}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['author'], data['author'])

    def test_menu_destroy(self):

        #Make a DELETE request to the detail view and check the status code
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 """