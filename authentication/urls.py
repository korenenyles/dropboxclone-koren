from django.urls import path, include
from django.contrib import admin
from authentication import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="loginpage"),
    path('logout/', views.LogoutView.as_view()),
    path('signup/', views.SignUpView.as_view(), name="signuppage")
]