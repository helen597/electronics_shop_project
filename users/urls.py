from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="login"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
