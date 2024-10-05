from typing import override

from django.db.models import Q
from rest_framework import generics, parsers, status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, ListAPIView, mixins
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import Profile

from .models import Post, Tag
from .permissions import IsOwnerOrReadOnly, ReadOnlyWriteOnlyByAuthor
from .serializers import (PostSerializer, SavedPostsSerializer,
                          SearchResultSerializer, TagSerializer)


class CreatePostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)

# class CreatePostView(APIView):
#     authentication_classes = [
#         JWTAuthentication,
#     ]
#     permission_classes = [
#         IsAuthenticated,
#     ]
#
#     http_method_names = ["post"]
#
#     def post(self, request):
#         try:
#             data = JSONParser().parse(request)
#             serializer = PostSerializer(data=data, context={'request': request})
#             if serializer.is_valid(raise_exception=True):
#                 print(serializer.validated_data)
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         except ParseError:
#             return Response(
#                 {"error": "parser error"}, status=status.HTTP_400_BAD_REQUEST
#             )


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication, ]
    permission_classes = [ReadOnlyWriteOnlyByAuthor, ]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):

        post = generics.get_object_or_404(Post, id=kwargs.get('pk'))
        user = request.user
        if user.is_authenticated:
            post.viewer.add(user)
        return super().get(request, *args, **kwargs)



class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagsView(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchView(APIView):

    def get(self, request):
        querry = request.GET.get('q')

        results = []

        if querry:
            results = Post.objects.filter(Q(title__icontains=querry) | Q(content__icontains=querry))
            serializer = SearchResultSerializer(results, many=True)
            return Response(serializer.data)


class SavedPosts(ListAPIView):

    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return  profile.saved_post.all()

    def list(self, request, *args, **kwargs):

        serializer = SavedPostsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class MyPostsListView(APIView):

    def get(self, request):
        posts = Post.objects.all().filter(author=request.user)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListByTagView(APIView):

    def get(self, request, tag):
        tag = generics.get_object_or_404(Tag, name=tag)
        posts = Post.objects.all().filter(tags=tag)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
