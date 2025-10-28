from django.db import models

# Create your models here.
class Usermodel(models.Model):
   username = models.CharField(null = True)
   email = models.CharField(blank = False)
   address = models.CharField(max_length= 150)
   updated_at = models.DateTimeField(auto_now=True)