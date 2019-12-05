from django.contrib.auth.models import AbstractUser, User
from django.db import models

from easyserializer import SerializeableObject


class Document(SerializeableObject, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    @property
    def updated_time(self):
        return self.updated_at.strftime('%Y-%m-%d %H:%M')

    @property
    def created_time(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')

