from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import Vote


class VoteSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    content_type = serializers.SlugRelatedField(
        slug_field='model', queryset=ContentType.objects.all()
    )
    object_id = serializers.IntegerField()

    class Meta:
        model = Vote
        fields = ['user', 'type', 'content_type', 'object_id']

    def create(self, validated_data):

        content_type = validated_data.pop('content_type')
        object_id = validated_data.pop('object_id')
        vote = Vote.objects.create(
            content_type=content_type,
            object_id=object_id,
            **validated_data
        )
        return vote

    def update(self, instance, validated_data):

        print(validated_data)
        print(instance.type, instance.content_type, instance.object_id)

        if instance.content_type == validated_data.get('content_type'):
            if instance.type != validated_data.get('type'):
                instance.type = validated_data.get('type', instance.type)
                instance.save()
        return instance
