from django.db import models


class User(models.Model):
    """ユーザモデル"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class WorkOut(models.Model):
    """筋トレの記録モデル"""

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_at = models.DateTimeField(auto_now_add=True)