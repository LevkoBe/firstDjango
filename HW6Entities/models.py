# models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    reminder = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - Status: {'Completed' if self.completed else 'Pending'}"

    class Meta:
        app_label = 'HW6Entities'
