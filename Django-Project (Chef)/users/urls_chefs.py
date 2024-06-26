from django.urls import path
from .views import ChefRegisterView, ChefLoginView, chef_profile, chef_dashboard

urlpatterns = [
    path('register/', ChefRegisterView.as_view(), name='chef-register'),
    path('login/', ChefLoginView.as_view(), name='chef-login'),
    path('profile/', chef_profile, name='chef-profile'),
    path('dashboard/', chef_dashboard, name='chef-dashboard'),
]
