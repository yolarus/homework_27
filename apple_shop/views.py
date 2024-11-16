from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product, Category, ContactData


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
        if i == 4:
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

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"categories": categories,
               "products": products}

    return render(request, "apple_shop/categories.html", context=context)


def product_detail(request: HttpRequest, pk: int):
    """
    Рендер страницы товара в интернет-магазине
    """
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "apple_shop/product_detail.html", context=context)


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

    contact = ContactData.objects.get(id=1)

    return render(request, "apple_shop/contacts.html", context={"contact": contact})
