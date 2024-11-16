from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Модель категорий товаров интернет-магазина для работы с БД
    """
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")
    photo = models.ImageField(upload_to="apple_shop/categories/photo", blank=True, null=True,
                              verbose_name='Фото')

    def __str__(self):
        """
        Метод для пользовательского вывода объекта модели
        """
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ['name']


class Product(models.Model):
    """
    Модель товаров интернет-магазина для работы с БД
    """
    name = models.CharField(max_length=150, verbose_name="Наименование товара")
    description = models.TextField(verbose_name="Описание товара")
    photo = models.ImageField(upload_to="apple_shop/products/photo",
                              blank=True,
                              null=True,
                              verbose_name="Изображение товара")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", related_name="products")
    price_per_unit = models.IntegerField(verbose_name="Цена за штуку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        """
        Метод для пользовательского вывода объекта модели
        """
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ['name']


class ContactData(models.Model):
    """
    Модель для хранения контактных данных
    """
    address = models.CharField(null=True, max_length=150, default="Адреса нет", verbose_name="Адрес")
    phone_number = models.CharField(null=True, max_length=50,
                                    default="Телефонов для связи нет", verbose_name="Телефон")
    email = models.CharField(null=True, max_length=100, default="Почты тоже нет", verbose_name="Почта")
    description = models.TextField(null=True, verbose_name="Описание",
                                   default="И гарантии нет "
                                           "\nКак и самих товаров "
                                           "\nЕсли что-то купили - покупайте еще "
                                           "\nИ друзьям предлагайте")

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"
