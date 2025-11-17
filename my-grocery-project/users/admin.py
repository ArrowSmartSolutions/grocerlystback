from django.contrib import admin
from .models import UserPermission

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'grocery_list', 'permission_level')
    search_fields = ('user__username', 'grocery_list__title')