from django.contrib.contenttypes.models import ContentType
from posts.models import Post
from posts.serializers import AuthorSerializer
from rest_framework import serializers
from votes.models import Vote

from .models import Comment


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
        post_content_type = ContentType.objects.get_for_model(Comment)
        return  Vote.objects.filter(content_type=post_content_type, object_id=obj, type=1).count()

    def get_downvotes(self, obj):
        post_content_type = ContentType.objects.get_for_model(Comment)
        return  Vote.objects.filter(content_type=post_content_type, object_id=obj, type=-1).count()



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_details = AuthorSerializer(source='author', read_only=True)
    replies = serializers.SerializerMethodField(read_only=True)

    id = serializers.IntegerField(read_only=True, source='pk')
    votes = VotesCountSerializer(source='pk', read_only=True)
    is_voted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['author', 'post', 'parent', 'id', 'content', 'created_at', 'updated_at', 'replies', 'author_details', 'votes', 'is_voted']


    def get_replies(self, obj):
        replies = Comment.objects.filter(parent=obj)
        # Pass the context when instantiating the nested serializer
        return CommentSerializer(replies, many=True, context=self.context).data


    def get_is_voted(self, obj):

        user = self.context['request'].user
        post_content_type = ContentType.objects.get_for_model(Comment)

        if user.is_authenticated:
            vote = Vote.objects.filter(user=user, content_type=post_content_type, object_id=obj.id).first()
            if vote:
                return IsVotedSerializer(vote).data

        return {'id': None, 'type': None}
