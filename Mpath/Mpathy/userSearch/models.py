from django.db import models

# Create your models here.
class users(models.Model):
      userName = models.CharField(max_length=120)
      description = models.TextField()
      boolTest = models.BooleanField(default=False)

      def _str_(self):
        return self.title