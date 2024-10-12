from django.urls import path
from . import views
from apple_shop.apps import AppleShopConfig

app_name = AppleShopConfig.name

urlpatterns = [
    path("", views.index, name="index"),
]
