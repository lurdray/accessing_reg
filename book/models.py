from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app.models import AppUser

class Book(models.Model):
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True)
    
    title = models.CharField(default="", max_length=200)
    author = models.CharField(default="", max_length=200)
    year = models.CharField(default="", max_length=10)

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
