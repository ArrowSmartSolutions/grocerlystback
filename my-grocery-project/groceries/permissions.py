import logging
from rest_framework import permissions
from .services import can_read, can_edit

logger = logging.getLogger(__name__)

class HasListAccess(permissions.BasePermission):
    """
    Object permission that delegates to groceries.services for permission checks.
    Denies safe access by default on errors and logs failures.
    """

    def has_object_permission(self, request, view, obj):
        try:
            # Owner always allowed
            if getattr(obj, 'owner', None) == request.user:
                return True

            # Read methods
            if request.method in permissions.SAFE_METHODS:
                return can_read(obj, request.user)

            # Write methods
            return can_edit(obj, request.user)

        except Exception as exc:
            logger.exception("HasListAccess unexpected error: %s", exc)
            return False