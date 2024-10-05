from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Vote
from .serializers import VoteSerializer


class VoteView(APIView):
    authentication_classes = [ JWTAuthentication,]
    permission_classes = [ IsAuthenticated,]

    http_method_names = ["post", "put", "delete"]

    def get_vote(self, pk):
        try:
            return  Vote.objects.get(pk=pk)
        except Vote.DoesNotExist:
            raise ValidationError({'error': 'vote does not exist'})


    def post(self, request):

        data = JSONParser().parse(request)
        serializer = VoteSerializer(data=data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            vote = serializer.save()
            return Response({"id": vote.pk, "type": vote.type})
        return Response(serializer.errors)


    def put(self, request, pk):
        vote = self.get_vote(pk)
        data = JSONParser().parse(request)
        serializer = VoteSerializer(instance=vote, data=data, context={"request": request})
        if serializer.is_valid():
            vote = serializer.save()
            return Response({"id": vote.pk, "type": vote.type})
        return Response(serializer.errors)
    

    def delete(self, request, pk):
        vote = self.get_vote(pk)
        vote.delete()
        return Response({"success":"Vote Deleted"})
