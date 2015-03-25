from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='owner')
    title = models.CharField(max_length=250, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ('created',)