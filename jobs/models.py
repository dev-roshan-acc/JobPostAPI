from django.db import models
from django.conf import settings


class Job(models.Model):
    # LOCATION_TYPE_CHOICES = [
    #     ("in_person", "In person"),
    #     ("remote", "Fully remote: no on-site work required"),
    #     ("hybrid", "Hybrid: some on-site work required"),
    #     ("on_the_road", "On the road"),
    # ]
    
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
    # location_type = models.CharField(
    #     max_length=20,
    #     choices=LOCATION_TYPE_CHOICES,
    #     default='in_person'
    # )
    
    # planned_start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


# Create your models here.
