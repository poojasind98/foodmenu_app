from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location = models.CharField(max_length=1000)

    def __str_(self):
        return self.user.username