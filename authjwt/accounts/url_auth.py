from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterAPI, LogoutAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutAPI.as_view(), name='logout'),
]


"""
http://localhost:8500/authapp/api/register/
http://localhost:8500/authapp/api/login/
http://localhost:8500/authapp/api/logout/
"""