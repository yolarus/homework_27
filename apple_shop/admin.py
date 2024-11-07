from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс для отображения модели Product в интерфейсе админки
    """
    list_display = ("id", "name", "price_per_unit", "category")
    list_filter = ("category", )
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс для отображения модели Category в интерфейсе админки
    """
    list_display = ("id", "name")
    search_fields = ("name", "description")
