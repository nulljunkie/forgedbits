import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from notifications import consumers, routing
from notifications.middlewares import JwtAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Set up the ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # WSGI for HTTP requests
    "websocket": JwtAuthMiddleware(
        URLRouter([
            # routing.websocket_urlpatterns,
            path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
        ])
    )
})

