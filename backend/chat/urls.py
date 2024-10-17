from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat_activate_view'),
    path('messages/<int:pk>', views.MessageListView.as_view(), name='chat_messages_list_view'),
]
