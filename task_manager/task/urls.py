from rest_framework import routers
from .views import TaskModelViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', TaskModelViewSet)

urlpatterns = [
   path('', include(router.urls))
]