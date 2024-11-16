from django.core.management import call_command
from django.core.management.base import BaseCommand

from apple_shop.models import ContactData


class Command(BaseCommand):
    """
    Заполнение БД фикстурой товаров интернет-магазина
    """

    def handle(self, *args: list, **kwargs: dict) -> None:
        ContactData.objects.all().delete()
        call_command('loaddata', 'contacts.json')

        self.stdout.write(self.style.SUCCESS("Фикстуры из файла contacts.json успешно загружены"))
