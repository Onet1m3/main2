from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import RegistrationForm
from .models import User

class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    success_message = 'Successfully registered'


class SigninView(LoginView):
    template_name = 'account/login.html'

class ProfileView(DetailView):
    model = User
    template_name = 'account/profile.html'


def index(request):
    return HttpResponse('Hello world')