from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from apps.forms import RegisterModelForm
from apps.models import Profile


class ListPage(ListView):
    queryset = Profile.objects.all()
    template_name = 'apps/login/profile.html'
    context_object_name = 'profiles'
    paginate_by = 3


class Register(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/login/register.html'
    success_url = 'login'


class Login(LoginView):
    template_name = 'apps/login/login.html'
    login_url = 'login_view'
