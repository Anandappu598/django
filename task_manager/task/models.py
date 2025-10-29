from django.db import models


# Create your models here.

class User(models.Model):
   username = models.CharField(max_length=100, blank=False, null=False)
   email = models.EmailField(unique=True)
   created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
   name = models.CharField(null=True, blank=True)
   status = models.BooleanField(default=False)

   user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
   