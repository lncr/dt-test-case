from rest_framework import serializers

from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='author.username')
    post_name = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'post_name', 'content', 'creation_date', ]
        read_only_fields = ['creation_date', ]
