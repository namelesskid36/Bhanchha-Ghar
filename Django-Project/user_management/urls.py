from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import index
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Map root URL to index view
    path('users/', include('users.urls')),  # Include app-specific URLs
    path('login/', CustomLoginView.as_view(), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # Logout page
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),  # Password reset
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),  # Password reset confirm
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),  # Password reset complete
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),  # Password change
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),  # Social auth
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
