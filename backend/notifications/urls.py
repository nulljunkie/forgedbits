from django.urls import path

from .views import ItemAPIView

urlpatterns = [
    path('create/', ItemAPIView.as_view(), name="api_create_item"),
    path('', ItemAPIView.as_view(), name="api_list_items"),
    path('item/<int:pk>', ItemAPIView.as_view(), name="api_item_view")
]
