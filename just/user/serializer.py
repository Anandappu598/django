from rest_framework import serializers

from .models import Usermodel , Admin
class AdminSer(serializers.ModelSerializer):
   class Meta:
      model = Admin
      field = '__all__'


class userserializer(serializers.ModelSerializer):
   admin = serializers.ReadOnlyField(source = 'admin.admin_name')
   class Meta:
      model = Usermodel
      field = '__all__'