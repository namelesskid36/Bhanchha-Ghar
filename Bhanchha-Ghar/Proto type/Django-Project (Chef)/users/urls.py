from django.urls import path
from .views import RegisterView, CustomLoginView, ChefRegisterView, ChefLoginView, chef_profile, chef_dashboard

urlpatterns = [
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', profile, name='users-profile'),

    path('chef/register/', ChefRegisterView.as_view(), name='chef-register'),
    path('chef/login/', ChefLoginView.as_view(), name='chef-login'),
    path('chef/profile/', chef_profile, name='chef-profile'),
    path('chef/dashboard/', chef_dashboard, name='chef-dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
