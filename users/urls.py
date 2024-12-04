from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="apple_shop:index"), name="logout"),
    path("email-confirm/<str:token>/", views.email_verification, name="email-confirm"),
    path("profile/<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]
