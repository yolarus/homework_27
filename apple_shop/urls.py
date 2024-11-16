from django.urls import path

from apple_shop.apps import AppleShopConfig

from . import views

app_name = AppleShopConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("categories/", views.categories, name="categories"),
    path("category_detail/<int:pk>", views.category_detail, name="category_detail"),
    path("product_detail/<int:pk>", views.product_detail, name="product_detail"),
    path("contacts/", views.contacts, name="contacts"),
    path("owner/", views.owner, name="owner"),
]
