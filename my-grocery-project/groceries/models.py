from django.db import models
from django.contrib.auth.models import User

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grocery_list = models.ForeignKey('groceries.GroceryList', on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=10, choices=[
        ('OWNER', 'Owner'),
        ('EDIT', 'Edit'),
        ('VIEW', 'View'),
    ])

    class Meta:
        unique_together = ('user', 'grocery_list')

    def __str__(self):
        return f"{self.user.username} - {self.permission_level} access to {self.grocery_list.title}"