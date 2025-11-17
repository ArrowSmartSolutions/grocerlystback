from django.urls import path
from .views import GroceryListViewSet, ListItemViewSet

urlpatterns = [
    path('lists/', GroceryListViewSet.as_view({'get': 'list', 'post': 'create'}), name='grocery-list'),
    path('lists/<uuid:pk>/', GroceryListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='grocery-list-detail'),
    path('lists/<uuid:list_id>/items/', ListItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='list-item'),
    path('lists/<uuid:list_id>/items/<uuid:item_id>/', ListItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='list-item-detail'),
]