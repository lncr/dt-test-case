from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from posts.models import Post
from posts.serializers import PostSerializer
from comments.serializers import CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


    @action(methods=['post', ], serializer_class=CommentSerializer, detail=True)
    def comments(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        post = self.get_object()

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)
            return Response(serializer.data)

    @action(methods=['post', ], detail=True)
    def upvote(self, request, *args, **kwargs):
        post = self.get_object()
        post.upvotes_amount += 1
        post.save()
        serializer = self.get_serializer_class()(instance=post)
        return Response(serializer.data)

    @action(methods=['post', ], detail=True, permission_classes=[IsAdminUser, ])
    def drop_upvotes(self, request, *args, **kwargs):
        post = self.get_object()
        post.upvotes_amount = 0
        post.save()
        serializer = self.get_serializer_class()(instance=post)
        return Response(serializer.data)
