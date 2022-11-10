from django.contrib import admin
from django.urls import path, include
from .views import profileViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('api', views.profileViewSet,basename='profileapi')
# router.register(r'api/<pk>', views.profileViewSet,basename='api')

urlpatterns = [
    # path('api', profileView.as_view()),
    path('', include(router.urls)),
]