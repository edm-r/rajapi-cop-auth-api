from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<str:email>/', UserProfileView.as_view(), name='user-profile-by-email'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/deactivate/', DeactivateAccountView.as_view(), name='deactivate-account')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)