from django.db import models

# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length= 264)
    email = models.CharField(max_length= 246)
    password = models.CharField(max_length= 20)

    def __str__(self):
        return self.name 
