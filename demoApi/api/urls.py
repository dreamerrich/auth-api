from django.contrib import admin
from django.urls import path
from .views import profileView

urlpatterns = [
    path('api', profileView.as_view()),
]