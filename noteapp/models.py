from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class table(models.Model):
 name=models.CharField(max_length=50)
 email=models.EmailField()
 number=models.BigIntegerField()
 guest=models.CharField(max_length=100)

 message=models.CharField(max_length=50)

# noteapp/models.py



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
