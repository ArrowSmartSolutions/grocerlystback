import logging
from typing import Optional, Any

from django.contrib.auth import get_user_model

from users.models import UserPermission
from .models import GroceryList

logger = logging.getLogger(__name__)
User = get_user_model()

def get_permission_for_user(grocery_list: GroceryList, user: Any) -> Optional[str]:
    """
    Return permission_level string ('OWNER','EDIT','VIEW') or None.
    Catches DB errors and logs them; returns None on any failure.
    """
    if not user:
        return None

    try:
        perm = UserPermission.objects.filter(grocery_list=grocery_list, user=user).first()
        if perm:
            return perm.permission_level
        return None
    except Exception as exc:
        logger.exception(
            "Error fetching UserPermission for list %s user %s: %s",
            getattr(grocery_list, 'id', None),
            getattr(user, 'id', None),
            exc
        )
        return None

def can_read(grocery_list: GroceryList, user: Any) -> bool:
    try:
        if grocery_list.owner == user:
            return True
        level = get_permission_for_user(grocery_list, user)
        return level in ('VIEW', 'EDIT')
    except Exception as exc:
        logger.exception("can_read check failed: %s", exc)
        return False

def can_edit(grocery_list: GroceryList, user: Any) -> bool:
    try:
        if grocery_list.owner == user:
            return True
        level = get_permission_for_user(grocery_list, user)
        return level == 'EDIT'
    except Exception as exc:
        logger.exception("can_edit check failed: %s", exc)
        return False