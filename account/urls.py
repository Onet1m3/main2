from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegisterView, SigninView, ProfileView

urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name='register'),
    path('login/', SigninView.as_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('myprofile/', ProfileView.as_view(), name='profile')
]