from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #name = models.CharField(default="",max_length=200)
    #email = models.CharField(default="",max_length=200)

    status = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username