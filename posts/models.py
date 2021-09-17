from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    upvotes_amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id', ]
