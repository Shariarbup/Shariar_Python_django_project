from django.db import models

# Create your models here.
class User_s(models.Model):
    firts_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.EmailField()

    def __str__(self):
        return (self.firts_name +' '+ self.last_name)