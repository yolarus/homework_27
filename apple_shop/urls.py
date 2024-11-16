from django.urls import path
from . import views
from apple_shop.apps import AppleShopConfig

app_name = AppleShopConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("categories/", views.categories, name="categories"),
    path("category_detail/<int:pk>", views.category_detail, name="category_detail"),
    path("contacts/", views.contacts, name="contacts"),
    path("product_detail/<int:pk>", views.product_detail, name="product_detail"),
]
