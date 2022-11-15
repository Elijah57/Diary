from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sex = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.CharField(max_length=1000)
    project_name = models.CharField(max_length=128)
