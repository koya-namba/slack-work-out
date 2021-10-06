from django.db import models


class User(models.Model):
    """ユーザモデル"""

    slack_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WorkOut(models.Model):
    """筋トレの記録モデル"""

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_at = models.DateTimeField(auto_now_add=True)