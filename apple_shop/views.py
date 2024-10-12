from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Рендер главной страницы приложения
    """
    return render(request, "apple_shop/index.html")


def catalog(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "каталог" приложения
    """
    return render(request, "apple_shop/catalog.html")


def categories(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "категории" приложения
    """
    return render(request, "apple_shop/categories.html")
