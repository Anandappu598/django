from rest_framework import routers
from .views import Userview
from django.urls import path , include

router = routers.DefaultRouter()
router.register(r'',Userview)

urlpatterns = [
   path('',include(router.urls))
]