from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('userpage/', views.userpage, name="userpage")
]