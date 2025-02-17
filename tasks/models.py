from django.db import models

# Create your models here.

class Priority(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    #user
