from django.contrib.auth.models import User
from django.db import IntegrityError

def create_user_service(data: dict):
    """
    Service to create a user. Raises ValueError on invalid input or DB issues.
    """
    try:
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        user.save()
        return user
    except KeyError as e:
        raise ValueError(f"Missing field: {e.args[0]}")
    except IntegrityError:
        raise ValueError("Failed to create user: database integrity error.")