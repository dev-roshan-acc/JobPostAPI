from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager

# Register your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_employer = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.username