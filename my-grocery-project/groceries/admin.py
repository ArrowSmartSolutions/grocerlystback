from django.contrib import admin
from .models import GroceryList, ListItem, ListAccess

admin.site.register(GroceryList)
admin.site.register(ListItem)
admin.site.register(ListAccess)