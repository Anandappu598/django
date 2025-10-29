from rest_framework import routers
from .views import TaskModelViewSet, UserModelViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TaskModelViewSet)
router.register(r'users', UserModelViewSet)

urlpatterns = [
   path('', include(router.urls))
]