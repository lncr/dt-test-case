from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
