from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register', views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        authentication_form=UserLoginForm), name='login'),
]
