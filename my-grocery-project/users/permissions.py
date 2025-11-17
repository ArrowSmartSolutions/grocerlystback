from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a grocery list to edit it.
    Others can only view the list.
    """

    def has_object_permission(self, request, view, obj):
        # Allow owners full access
        if obj.owner == request.user:
            return True

        # Allow read-only access for others
        return request.method in permissions.SAFE_METHODS


class CanEditList(permissions.BasePermission):
    """
    Custom permission to allow users with 'EDIT' access to modify grocery lists.
    """

    def has_permission(self, request, view):
        # Check if the user has 'EDIT' access
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow owners and users with 'EDIT' access to modify the list
        if obj.owner == request.user:
            return True

        try:
            access = ListAccess.objects.get(list=obj, user=request.user)
            return access.permission_level == 'EDIT'
        except ListAccess.DoesNotExist:
            return False


class CanViewList(permissions.BasePermission):
    """
    Custom permission to allow users with 'VIEW' access to view grocery lists.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow owners and users with 'VIEW' access to view the list
        if obj.owner == request.user:
            return True

        try:
            access = ListAccess.objects.get(list=obj, user=request.user)
            return access.permission_level in ['VIEW', 'EDIT']
        except ListAccess.DoesNotExist:
            return False