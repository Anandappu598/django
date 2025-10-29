from rest_framework import serializers

# Importing the models from models file
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):

   class Meta:
      model=User
      fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
   user = serializers.CharField()

   class Meta:
      model=Task
      fields = '__all__'