from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product, Category


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Рендер главной страницы приложения
    """
    latest_products = Product.objects.all().order_by("-updated_at")
    products_list = []
    for i, product in enumerate(latest_products):
        products_list.append(product)
        print(product)
        if index == 4:
            break

    return render(request, "apple_shop/index.html", context={"products": products_list[:3]})


def catalog(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "каталог" приложения
    """
    return render(request, "apple_shop/catalog.html")


def categories(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "категории" приложения
    """

    iphone_category = Category.objects.get(name="Iphone")

    latest_iphones = Product.objects.filter(category=iphone_category).order_by("-updated_at")
    iphones_list = []
    for i, iphone in enumerate(latest_iphones):
        iphones_list.append(iphone)
        print(iphone)

    return render(request, "apple_shop/categories.html", context={"iphones": iphones_list[:6]})


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
