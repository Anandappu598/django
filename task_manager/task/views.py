from django.shortcuts import render

from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

# For Creating View
from rest_framework import viewsets

class UserModelViewSet(viewsets.ModelViewSet):

   queryset = User.objects.all()
   serializer_class = UserSerializer


# Create your views here.
class TaskModelViewSet(viewsets.ModelViewSet):

   queryset=Task.objects.all()
   serializer_class = TaskSerializer