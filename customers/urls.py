from django.contrib import admin
from django.urls import path, include
from .views import UserSignUpView, UserSignInView

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("signin/", UserSignInView.as_view(), name="signin"),
]
