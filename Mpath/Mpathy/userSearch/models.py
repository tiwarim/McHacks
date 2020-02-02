from django.db import models
from datetime import datetime

# Create your models here.
#   need to be moved
class User_Account(models.Model):
    user_name = models.CharField(max_length=200)
    pass_wd = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user_name

class Supervisee(models.Model):
    user = models.ForeignKey(User_Account, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=200, default='twitter')
    social_media_id = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name