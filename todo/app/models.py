from django.db import models
from django.contrib.auth.models import User


class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
