from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Notification
from .serializers import NotificationSerializer


class NotificationView(ListAPIView, UpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [] # IsOwner
    serializer_class = NotificationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Notification.objects.all().filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        user= self.request.user
        count = user.notifications_mine.count()
        unread_count =  user.notifications_mine.filter(is_read=False).count()
        return Response({ 'count': count, 'unread_count': unread_count, 'items': serializer.data})

class UnreadNotificationCountView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        unread_count =  request.user.notifications_mine.filter(is_read=False).count()
        return Response({'unread_count': unread_count})
