from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

# For Creating View
from rest_framework import viewsets

# Create your views here.
class TaskModelViewSet(viewsets.ModelViewSet):

   queryset=Task.objects.all()
   serializer_class = TaskSerializer