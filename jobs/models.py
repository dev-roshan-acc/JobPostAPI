from django.db import models
from django.conf import settings


class Job(models.Model):
    employer= models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="jobs"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    salary = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    location= models.ForeignKey(
        "locations.Location", on_delete=models.CASCADE, related_name="jobs"
    )

    def __str__(self):
        return self.title


# Create your models here.
