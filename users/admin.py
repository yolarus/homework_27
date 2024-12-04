from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс для отображения модели User в интерфейсе админки
    """
    list_display = ("id", "email", "username", "phone_number")
