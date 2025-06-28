from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.city}, {self.country}"
