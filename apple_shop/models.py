from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Модель категорий товаров интернет-магазина для работы с БД
    """
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории")

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
    image = models.ImageField(upload_to="apple_shop/products_images",
                              blank=True,
                              null=True,
                              verbose_name="Изображение товара")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
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
