from rest_framework import serializers

from .models import Profile, User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserInfoSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileSerializer(serializers.ModelSerializer):
    # hidden field for write only it uses context
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    image = serializers.ImageField(required=False, use_url=True)
    banner = serializers.ImageField(required=False, use_url=True)
    bio = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    website = serializers.URLField(required=False)
    linkedin_profile = serializers.URLField(required=False)
    github_profile = serializers.URLField(required=False)
    firstName = serializers.CharField(source='user.first_name', required=False)
    lastName = serializers.CharField(source='user.last_name', required=False)
    email = serializers.CharField(source='user.email', required=False)
    username = serializers.CharField(source='user.username', required=False)
    birth_date = serializers.DateField(source='user.birth_date', required=False)

    class Meta:
        model = Profile
        fields = ["user", "image", "banner", "bio", "firstName", "lastName", "email", "username", "location", "phone_number", "website", "linkedin_profile", "github_profile", "birth_date"]


    def is_valid(self, *, raise_exception=False):

          
        user_data = {
            'first_name': self.initial_data.pop('firstName', None),
            'last_name': self.initial_data.pop('lastName', None),
            'email': self.initial_data.pop('email', None),
            'username': self.initial_data.pop('username', None),
            'birth_date': self.initial_data.pop('birth_date', None),
        }


        print('data: ', user_data)
        # serializer = UserInfoSerializer(data=user_data)

        # if serializer.is_valid(raise_exception=True):
        #     print('user valid data: ', serializer.validated_data)
        # print('not vvalid fucking data')

        user = self.context['request'].user

        if user_data['first_name'] is not None:
            user.first_name = user_data['first_name']
        if user_data['last_name'] is not None:
            user.last_name = user_data['last_name']
        if user_data['email'] is not None:
            user.email = user_data['email']
        if user_data['username'] is not None:
            user.username = user_data['username']
        if user_data['birth_date'] is not None:
            user.birth_date = user_data['birth_date']

        user.save()

        return super().is_valid(raise_exception=raise_exception)



class ProfileGlimpsSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False, use_url=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)

    is_followed = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['bio', 'email', 'is_followed', 'first_name', 'last_name', 'date_joined', 'image', 'username', 'id', 'followers', 'following', 'posts_count', 'comments_count']


    def get_is_followed(self, obj):

        user = self.context['request'].user
        if user.is_authenticated:
            return obj.followers.all().filter(user=user).exists()
        return False

    def get_followers(self, obj):
        return obj.followers.all().count()

    def get_following(self, obj):
        return obj.follower.all().count()

    def get_posts_count(self, obj):
        return obj.user.posts.all().count()

    def get_comments_count(self, obj):
        return obj.user.comments.all().count()


