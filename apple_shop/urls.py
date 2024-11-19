from django.urls import path

from apple_shop.apps import AppleShopConfig

from . import views

app_name = AppleShopConfig.name

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("catalog/", views.CatalogListView.as_view(), name="catalog"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("product/detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("contacts/<int:pk>/", views.ContactsDetailView.as_view(), name="contacts"),
    path("owner/", views.ProductCreateView.as_view(), name="owner"),
]
