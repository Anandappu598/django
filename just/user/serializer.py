from rest_framework import serializers

from .models import Usermodel
class userserializer(serializers.ModelSerializer):
   class meta:
      model = Usermodel
      field = '__all__'