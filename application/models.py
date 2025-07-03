from django.db import models
from jobs.models import Job
from django.conf import settings

# Create your models here.


class Application(models.Model):
    STATUS_CHOOSE = [
        ("applied", "Applied"),
        ("withdrawn", "Withdrawn"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="application")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="application"
    )
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOOSE, max_length=10, default="applied")
    applied_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job','user')  # prevent duplicate application

    def __str__(self):
        return f"{self.user.username} -> {self.job.title} "
