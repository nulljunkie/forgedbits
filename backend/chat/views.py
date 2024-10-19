from django.db.models import Q
from rest_framework import generics
from rest_framework.fields import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Chat, Message
from .permissions import IsUserInvolvedInChat
from .serializers import ChatSerializer, MessageSerializer


# TODO: fix the permissions, can create chat of other users
class ChatView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsUserInvolvedInChat,]
    serializer_class = ChatSerializer

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(alice=user) | Q(bob=user))


#TODO: add permissions get only chats of given pk, where only authenticated user is alice or bob
class MessageListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication,]
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        queryset = Message.objects.filter(chat=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

