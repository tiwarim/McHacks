from django.db import models

# Create your models here.
#   need to be moved
class User_Account(models.Model):
    user_name = models.CharField(max_length=200)
    pass_wd = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    create_date = models.DateField()

    def __str__(self):
        return self.user_name

class User_Target():
    user = models.ForeignKey(User_Account, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=200, default='twitter')
    social_media_id = models.CharField(max_length=200)
