from django.contrib.auth.models import AbstractUser
from django.db import models

# Register your models here.

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=False)
    

    def __str__(self):
        return self.username