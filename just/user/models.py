from django.db import models

# Create your models here.

class Admin(models.Model):
   admin_name = models.CharField(null = False)

class Usermodel(models.Model):
   username = models.CharField(null = True)
   email = models.CharField(blank = False)
   address = models.CharField(max_length= 150)
   updated_at = models.DateField(auto_now=True)
   admin = models.ForeignKey(Admin ,on_delete=models.CASCADE,blank=False,null=False)

