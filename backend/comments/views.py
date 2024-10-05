from posts.models import Post
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Comment
from .serializers import CommentSerializer


class CommentView(APIView):

    http_method_names = ["get"]

    def get(self, request, post_id):

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response("post does not exist")


        comments = Comment.objects.filter(post=post).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True, context={'request': request})

        comment_list = []

        for comment in serializer.data:
            if not comment.get('parent'):
                comment_list.append(comment)

        # return Response(serializer.data)
        return Response(comment_list)


class CreateCommentView(APIView):

    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]

    http_method_names = ["post"]

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CommentSerializer(data=data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                print(serializer.validated_data)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ParseError:
            return Response(
                {"error": "parser error"}, status=status.HTTP_400_BAD_REQUEST
            )
