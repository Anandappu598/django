from rest_framework import serializers

# Importing the models from models file
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

   class Meta:
      model=Task
      fields = ['name','status']