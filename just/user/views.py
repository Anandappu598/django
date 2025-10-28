from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import userserializer
from .models import Usermodel

class Userview(viewsets.ModelViewSet):
   queryset = Usermodel.objects.all()
   serializer_class = userserializer