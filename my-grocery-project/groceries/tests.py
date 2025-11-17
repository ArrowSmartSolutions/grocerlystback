from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import GroceryList, ListAccess

User = get_user_model()

class GroceryListModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.grocery_list = GroceryList.objects.create(title='Weekly Groceries', owner=self.user)

    def test_grocery_list_creation(self):
        self.assertEqual(self.grocery_list.title, 'Weekly Groceries')
        self.assertEqual(self.grocery_list.owner, self.user)

class ListAccessModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass1')
        self.user2 = User.objects.create_user(username='user2', password='pass2')
        self.grocery_list = GroceryList.objects.create(title='Weekly Groceries', owner=self.user1)
        self.list_access = ListAccess.objects.create(list=self.grocery_list, user=self.user2, permission_level='VIEW')

    def test_list_access_creation(self):
        self.assertEqual(self.list_access.list, self.grocery_list)
        self.assertEqual(self.list_access.user, self.user2)
        self.assertEqual(self.list_access.permission_level, 'VIEW')