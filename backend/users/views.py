import requests
from django.conf import settings
from posts.models import Post
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .exceptions import WeakPasswordError
from .models import Profile, User
from .serializers import ProfileGlimpsSerializer, ProfileSerializer


# todo: most of the work done here should be in serializers.py
class RegisterView(APIView):
    def post(self, request):
        username = request.data["username"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        if username is not None:
            try:
                User.objects.get(pk=username)
            except User.DoesNotExist:
                if password1 == password2:
                    try:
                        user = User.objects.create_user(username, password1)
                    except WeakPasswordError:
                        return Response(
                            {"WEAKPASSWORD": "your password is weak"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    else:
                        if user is not None:
                            user.save()
                            refresh = RefreshToken.for_user(user)
                            return Response(
                                {
                                    "access": str(refresh.access_token),
                                    "refresh": str(refresh),
                                },
                                status=status.HTTP_201_CREATED,
                            )
                return Response(
                    {"NOMATCH": "passwords do not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    {"EXISTS": f"{username} is taken"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            {"EMPTY": "username is none"}, status=status.HTTP_400_BAD_REQUEST
        )


class UpdateProfileView(APIView):
    # parser_classes = [FileUploadParser]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     try:
    #         # is this defined also in except and else
    #         profile = Profile.objects.get(user=request.user)
    #     except Profile.DoesNotExist:
    #         serializer = ProfileSerializer(
    #             data=request.data, context={"request": request}
    #         )
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         serializer = ProfileSerializer(
    #             instance=profile, data=request.data, context={"request": request}
    #         )
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):

        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(
            instance=profile, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    # parser_classes = [FileUploadParser]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response(
                {"not_valid": "profile does not exits"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = ProfileSerializer(
                profile, many=False, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)


class SavePostView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response(
                {"not_valid": "post does not exits"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            profile = Profile.objects.get(user=request.user)
            profile.saved_post.add(post)
            return Response({'Done': 'post added to your saved posts'}, status=status.HTTP_200_OK)

    def delete(self, request):

        post_id = request.data.get('post_id')
        post = Post.objects.get(pk=post_id)
        profile = Profile.objects.get(user=request.user)

        profile.saved_post.remove(post)
        return Response({'Done': 'removed from saved post'}, status=status.HTTP_200_OK)



class ProfileGlimpsAPIView(generics.RetrieveAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileGlimpsSerializer
    lookup_field = 'pk'



class FollowAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_me_and_other(self, request):
        self.my_profile = generics.get_object_or_404(Profile, user=request.user)
        
        profile_id = request.data.get('profile_id')
        if profile_id is None:
            raise ValidationError("Profile ID is required.")
        
        self.profile_to_follow = generics.get_object_or_404(Profile, pk=profile_id)
        
        if self.my_profile == self.profile_to_follow:
            raise ValidationError("You cannot follow yourself.")


    def post(self, request, *args, **kwargs):
        self.get_me_and_other(request)
        # if self.profile_to_follow.followers.all().filter(user=self.my_profile.user).exists():
        #     self.profile_to_follow.followers.remove(self.my_profile)
        #     print(f'{self.my_profile.user.username} unfollowed {self.profile_to_follow.user.username}')
        #     return Response({"is_followed": False}, status=status.HTTP_202_ACCEPTED)
        self.profile_to_follow.followers.add(self.my_profile)
        print(f'{self.my_profile.user.username} is following {self.profile_to_follow.user.username}')
        return Response({"is_followed": True}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        self.get_me_and_other(request)
        self.profile_to_follow.followers.remove(self.my_profile)
        print(f'{self.my_profile.user.username} unfollowed {self.profile_to_follow.user.username}')
        return Response({"is_followed": False}, status=status.HTTP_202_ACCEPTED)



class UserListAPIView(generics.ListAPIView):

    authentication_classes = [JWTAuthentication]

    queryset = Profile.objects.all()
    serializer_class = ProfileGlimpsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        user = request.user
        if user.is_authenticated:
            queryset = queryset.exclude(user=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GithubLoginAPIView(APIView):

    def get(self, request):
        client_id = settings.GITHUB_CLIENT_ID
        redirect_uri = settings.GITHUB_REDIRECT_URI
        return Response({'oauth_url': f'https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}'})


class GithubAuthView(APIView):

    def post(self, request):
        code = request.data.get('code')
        client_id = settings.GITHUB_CLIENT_ID
        client_secret = settings.GITHUB_CLIENT_SECRET

        print(client_id)
        print(client_secret)
        print(code)

        token_response = requests.post('https://github.com/login/oauth/access_token', data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code
        }, headers={'Accept': 'application/json'})

        token_json = token_response.json()
        access_token = token_json.get('access_token')

        user_info_response = requests.get('https://api.github.com/user', headers={
            'Authorization': f'token {access_token}'
        })
        
        user_info = user_info_response.json()
        username = user_info.get('login')

        if username: 
            user, created = User.objects.get_or_create(username=username)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username,
            },
            status=status.HTTP_202_ACCEPTED,
        )
