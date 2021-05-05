from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` and 'exclude' argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            not_allowed = set(exclude)
            for exclude_name in not_allowed:
                self.fields.pop(exclude_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CommentSerializer(serializers.RelatedField):
    def to_native(self, value):
        return {str(value.pk): value.id}

    def to_representation(self, data):
        serializer = TweetSerializer(data)
        return serializer.data


class TweetSerializer(DynamicFieldsModelSerializer):
    account = UserSerializer(read_only=True)
    liked_by = UserSerializer(read_only=True, many=True)
    retweeted_by = UserSerializer(read_only=True, many=True)
    likes = serializers.IntegerField(source='get_likes', read_only=True)
    retweets = serializers.IntegerField(source='get_retweets', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_num = serializers.SerializerMethodField(read_only=True)

    def get_comments_num(self, tweet):
        return tweet.comments.count()

    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['created_at']
        # exclude = ['liked_by', 'retweeted_by', 'parent']
