from django.urls import path
from .views import home, index, RegisterView, CustomLoginView, ResetPasswordView, ChangePasswordView, profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # Landing page
    path('home/', home, name='home'),  # /home/ URL
    path('register/', RegisterView.as_view(), name='users-register'),  # Registration page
    path('profile/', profile, name='users-profile'),  # Profile page
    path('login/', CustomLoginView.as_view(), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # Logout page
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),  # Password reset
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),  # Password change
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
