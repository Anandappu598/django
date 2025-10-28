from django.db import models


# Create your models here.

class Task(models.Model):
   name = models.CharField(null=True, blank=True)
   status = models.BooleanField(default=False)