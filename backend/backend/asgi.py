import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django_asgi_app = get_asgi_application()

from chat.consumers import ChatConsumer
from notifications.consumers import NotificationConsumer
from notifications.middlewares import JwtAuthMiddleware

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # WSGI for HTTP requests
    "websocket": JwtAuthMiddleware(
        URLRouter([
            path('ws/notifications/', NotificationConsumer.as_asgi()),
            path('ws/chat/', ChatConsumer.as_asgi()),
        ])
    )
})

