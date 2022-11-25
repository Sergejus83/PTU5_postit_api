from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')
        
    class Meta:
            model = models.Comment
            fields = ('id', 'post', 'body', 'user', 'user_id', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = CommentSerializer(many=True)
        
    class Meta:
            model = models.Post
            fields = ('id', 'title', 'body', 'user', 'user_id', 'created_at', 'comments')

