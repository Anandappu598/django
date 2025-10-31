from rest_framework import routers
from .views import Userview,AdminView
from django.urls import path , include

router = routers.DefaultRouter()
router.register(r'user',Userview)
router.register(r'admin',AdminView)

urlpatterns = [
   path('',include(router.urls))
]