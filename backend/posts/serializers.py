import json

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from users.models import Profile, User
from votes.models import Vote

from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Tag
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile.image', read_only=True, use_url=True)
    profile_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['profile_id', 'username', 'image']

    def get_profile_id(self, obj):
        return obj.profile.id


class IsVotedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id', 'type']


class VotesCountSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vote
        fields = ['upvotes', 'downvotes']

    def get_upvotes(self, obj):
        post_content_type = ContentType.objects.get_for_model(Post)
        return  Vote.objects.filter(content_type=post_content_type, object_id=obj, type=1).count()

    def get_downvotes(self, obj):
        post_content_type = ContentType.objects.get_for_model(Post)
        return  Vote.objects.filter(content_type=post_content_type, object_id=obj, type=-1).count()

class PostSerializer(serializers.ModelSerializer):
    # write-only field
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # read-only filed
    author_details = AuthorSerializer(source='author', read_only=True)
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    cover = serializers.ImageField(required=False, use_url=True)
    is_draft = serializers.BooleanField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    id = serializers.IntegerField(read_only=True, source='pk')
    tags = TagSerializer(required=False, many=True)

    votes = VotesCountSerializer(source='id', read_only=True)

    is_voted = serializers.SerializerMethodField()

    views_count = serializers.SerializerMethodField(read_only=True)

    is_saved = serializers.SerializerMethodField(read_only=True)

    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "author_details", "title", "content", "tags", "views_count", "is_draft", "created_at", "updated_at", "votes", 'is_voted', 'is_saved', 'comments_count', 'cover']

    def create(self, validated_data):

        tags_data = json.loads(self.initial_data.get('tags', []))
        validated_data.pop('tags', None)  # Pop tags to prevent duplication in Post creation

        post = Post.objects.create(**validated_data)

        tag_instances = []
        for tag in tags_data:
            # tag_instance, created = Tag.objects.get_or_create(id=tag.get('id'), defaults={'name': tag['name']})
            tag_instance, created = Tag.objects.get_or_create(name=tag)
            tag_instance.posts_count += 1
            tag_instance.save()
            # print(tag_instance.name, f'[{tag_instance.posts_count}]')
            # if (created):
            #     print(tag_instance, 'created')

            tag_instances.append(tag_instance)

        post.tags.set(tag_instances)
        return post

    def get_is_voted(self, obj):

        user = self.context['request'].user
        post_content_type = ContentType.objects.get_for_model(Post)

        if user.is_authenticated:
            vote = Vote.objects.filter(user=user, content_type=post_content_type, object_id=obj.id).first()
            if vote:
                return IsVotedSerializer(vote).data

        return {'id': None, 'type': None}


    def get_views_count(self, obj):
        return obj.viewer.all().count()


    def get_is_saved(self, obj):

        user = self.context['request'].user

        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
            try:
                profile.saved_post.get(id=obj.pk)
                return True
            except Post.DoesNotExist:
                return False

        return False


    def get_comments_count(self, obj):
        return obj.comments.all().count()


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'id')


class SavedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'id')
