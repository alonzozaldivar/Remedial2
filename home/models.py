from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default="User", blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(default="user@gmail.com", blank=True, null=True)
    bio = models.CharField(max_length=256, default="Biography", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name