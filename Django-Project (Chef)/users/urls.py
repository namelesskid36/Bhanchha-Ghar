from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, index, RegisterView, CustomLoginView, ResetPasswordView, ChangePasswordView, profile
from django.contrib.auth import views as auth_views

import logging

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', index, name='index'),  # Landing page
    path('home/', home, name='home'),  # /home/ URL
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),  # Import and use 'profile' function
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for url_pattern in urlpatterns:
    logger.info(f'URL pattern: {url_pattern}')