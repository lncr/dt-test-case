from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    upvotes_amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id', ]

    @property
    def rating(self):
        ratings = self.ratings.all()
        if ratings:
            sum_ = 0
            for rating in ratings:
                sum_ += rating.value
            return round(sum_ / len(ratings), 2)
        return 0


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(validators=[
                                MaxValueValidator(5),
                                MinValueValidator(1)
                                ])
