from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
import datetime

# Create your models here.
class File(models.Model):
    uuid = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
     
    def __str__(self):
        return self.name

class FileVersion(models.Model):
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    main_file = models.ForeignKey(File)
    