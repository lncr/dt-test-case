from rest_framework import serializers
from posts.models import Post

from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'author_name', 'title', 'link', 'upvotes_amount', 'creation_date', 
                  'comments', ]
        read_only_fields = ['upvotes_amount', 'creation_date', ]
