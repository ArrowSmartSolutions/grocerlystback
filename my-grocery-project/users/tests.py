from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ListAccess, GroceryList

User = get_user_model()

class ListAccessModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.grocery_list = GroceryList.objects.create(title='Test List', owner=self.user)

    def test_create_list_access(self):
        access = ListAccess.objects.create(list=self.grocery_list, user=self.user, permission_level='EDIT')
        self.assertEqual(access.permission_level, 'EDIT')
        self.assertEqual(access.user, self.user)
        self.assertEqual(access.list, self.grocery_list)

    def test_list_access_permissions(self):
        ListAccess.objects.create(list=self.grocery_list, user=self.user, permission_level='VIEW')
        access = ListAccess.objects.get(user=self.user, list=self.grocery_list)
        self.assertEqual(access.permission_level, 'VIEW')

    def test_invalid_permission_level(self):
        with self.assertRaises(ValueError):
            ListAccess.objects.create(list=self.grocery_list, user=self.user, permission_level='INVALID')

    def test_user_can_access_own_list(self):
        access = ListAccess.objects.create(list=self.grocery_list, user=self.user, permission_level='EDIT')
        self.assertTrue(access.user == self.user)

    def test_user_cannot_access_other_users_list(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        access = ListAccess.objects.create(list=self.grocery_list, user=other_user, permission_level='VIEW')
        self.assertFalse(access.user == self.user)