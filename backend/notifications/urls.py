from django.urls import path

from .views import NotificationView, UnreadNotificationCountView

urlpatterns = [
    path('<int:pk>/', NotificationView.as_view(), name="notification_update_view"),
    path('', NotificationView.as_view(), name="notification_list_view"),
    path('unread-count/', UnreadNotificationCountView.as_view(), name="unread_notification_count_view"),
]
