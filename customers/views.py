from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import UserSignUpForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


class UserSignUpView(FormView):
    template_name = "customers/signup.html"
    success_url = reverse_lazy("home")
    form_class = UserSignUpForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Signed up successfully")
        return super().form_valid(form)


class UserSignInView(LoginView):
    template_name = "customers/signin.html"

    def get_success_url(self):
        messages.success(self.request, "Signed in successfully")
        return reverse_lazy("home")
