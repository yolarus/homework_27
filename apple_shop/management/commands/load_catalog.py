from django.core.management import call_command
from django.core.management.base import BaseCommand

from apple_shop.models import Category, Product


class Command(BaseCommand):
    """
    Заполнение БД фикстурой товаров интернет-магазина
    """

    def handle(self, *args: list, **kwargs: dict) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command('loaddata', 'catalog.json')

        self.stdout.write(self.style.SUCCESS("Фикстуры из файла catalog.json успешно загружены"))
