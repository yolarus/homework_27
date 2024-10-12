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


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "контакты" приложения
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Получено сообщение '{message}' от пользователя {name} ({email})")
        return HttpResponse("Ваше сообщение успешно отправлено!")

    return render(request, "apple_shop/contacts.html")
