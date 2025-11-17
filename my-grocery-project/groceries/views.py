from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import HasListAccess
from .services import can_edit

# Example: ensure GroceryListViewSet uses object-level permission
class GroceryListViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, HasListAccess]

# Example ListItemViewSet (nested under list). Ensure create/update enforce list permissions:
class ListItemViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, HasListAccess]  # object-level for parent list checks as well

    def perform_create(self, serializer):
        parent_list = serializer.validated_data.get('list')
        if not parent_list:
            # If you pass list via URL, resolve it from view kwargs instead
            parent_list = getattr(self, 'list_instance', None)
        if not can_edit(parent_list, self.request.user):
            raise PermissionDenied(detail="You do not have edit permission on this list.")
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        parent_list = serializer.instance.list
        if not can_edit(parent_list, self.request.user):
            raise PermissionDenied(detail="You do not have edit permission on this list.")
        serializer.save()