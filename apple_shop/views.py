from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Рендер главной страницы приложения
    """
    return render(request, "apple_shop/index.html")
