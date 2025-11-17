from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class UserPermission(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_permissions'
    )
    grocery_list = models.ForeignKey(
        'groceries.GroceryList',
        on_delete=models.CASCADE,
        related_name='user_permissions'
    )
    class PermissionLevel(models.TextChoices):
        OWNER = 'OWNER', _('Owner')
        EDIT = 'EDIT', _('Edit')
        VIEW = 'VIEW', _('View')

    permission_level = models.CharField(
        max_length=10,
        choices=PermissionLevel.choices,
        default=PermissionLevel.VIEW
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'grocery_list'], name='unique_user_grocery_permission')
        ]
        verbose_name = "User Permission"
        verbose_name_plural = "User Permissions"
        ordering = ['grocery_list', 'user']

    def __str__(self):
        try:
            return f"{self.user.username} - {self.permission_level} access to {self.grocery_list.title}"
        except Exception:
            return f"UserPermission(id={self.pk})"