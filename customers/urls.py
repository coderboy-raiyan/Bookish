from django.contrib import admin
from django.urls import path, include
from .views import UserSignUpView, UserSignInView, UserLogoutView, UserProfileView

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("signin/", UserSignInView.as_view(), name="signin"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("logout/", UserLogoutView.as_view(), name="logout")
]
