from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ActiveChat
from .permissions import IsChatParticipant, IsUserInvolvedInChatCreation
from .serializers import ChatSerializer

# TODO: fix the permissions

class ChatView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsChatParticipant, IsUserInvolvedInChatCreation]
    queryset = ActiveChat.objects.all()
    serializer_class = ChatSerializer

