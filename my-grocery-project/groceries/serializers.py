from rest_framework import serializers
from .models import UserPermission

class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ['id', 'user', 'grocery_list', 'permission_level']