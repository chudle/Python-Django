from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import *
from .models import *

class register( CreateView ):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def get_context_data(self, *, object_list = None, **kwargs ):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

class LoginUser( LoginView ):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list = None, **kwargs ):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()) )

def Logout_user(request):
    logout(request)
    return redirect('home')
