from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import userserializer,AdminSer
from .models import Usermodel,Admin

class AdminView(viewsets.ModelViewSet):
   queryset = Admin.objects.all()
   serializer_class = AdminSer
   
class Userview(viewsets.ModelViewSet):
   queryset = Usermodel.objects.all()
   serializer_class = userserializer