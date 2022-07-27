from django.urls import path, include
from .views import RegisterAPIView, ChangePasswordAPIView, UpdateUserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django_email_verification import urls as email_urls

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='registration'),
    path('email/', include(email_urls)),
    path('change_password/<int:pk>/', ChangePasswordAPIView.as_view(), name="password_change"),
    path('update_profile/<int:pk>/', UpdateUserProfileAPIView.as_view(), name='update_profile')
]