from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField

# Create your models here.
class File(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    file = models.FileField()
     
    def __str__(self):
        return self.name
