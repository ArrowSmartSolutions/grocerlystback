from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ListAccess

@receiver(post_save, sender=User)
def create_user_list_access(sender, instance, created, **kwargs):
    if created:
        # Automatically create a default ListAccess entry for new users
        ListAccess.objects.create(user=instance, permission_level='VIEW')  # Default permission level can be set here

@receiver(post_save, sender=User)
def save_user_list_access(sender, instance, **kwargs):
    instance.listaccess.save()  # Ensure the ListAccess entry is saved when the user is saved