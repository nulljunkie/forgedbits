from channels import auth
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth import get_user_model
from jwt import decode as jwt_decode
from jwt.exceptions import InvalidTokenError


class JwtAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = dict((x.split('=') for x in scope['query_string'].decode().split('&')))
        token = query_string.get('token')

        if token:
            try:
                # Decode JWT token and extract payload
                payload = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                
                user_id = payload['user_id']

                # beware pk = username in my case in User model
                user = await get_user(user_id)

                scope['user'] = user
            except InvalidTokenError:
                scope['user'] = None
        else:
            scope['user'] = None

        return await super().__call__(scope, receive, send)


@auth.database_sync_to_async
def get_user(user_id):

    from django.contrib.auth.models import AnonymousUser
    User = get_user_model()
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


def CustomAuthMiddlewareStack(inner):
    return JwtAuthMiddleware(auth.AuthMiddlewareStack(inner))

