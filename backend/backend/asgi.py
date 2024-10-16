import os

from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer
from django.core.asgi import get_asgi_application
from django.urls import path
from notifications.consumers import NotificationConsumer
from notifications.middlewares import JwtAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Set up the ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # WSGI for HTTP requests
    "websocket": JwtAuthMiddleware(
        URLRouter([
            # routing.websocket_urlpatterns,
            path('ws/notifications/', NotificationConsumer.as_asgi()),
            path('ws/chat/', ChatConsumer.as_asgi()),
        ])
    )
})

