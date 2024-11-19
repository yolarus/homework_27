from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Category, ContactData, Product


# Create your views here.
class IndexListView(ListView):
    """
    Класс-представление страницы "Главная"
    """
    model = Product
    template_name = "apple_shop/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-updated_at")


class CatalogListView(ListView):
    """
    Класс-представление страницы "Каталог"
    """
    model = Category
    template_name = "apple_shop/catalog.html"
    context_object_name = "categories"


class CategoryListView(ListView):
    """
    Класс-представление страницы "Категории"
    """
    model = Category
    template_name = "apple_shop/category_list.html"
    context_object_name = "categories"

    @staticmethod
    def get_products():
        """
        Получение всех товаров для вывода на страницу
        """
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["products"] = self.get_products()
        return context


class CategoryDetailView(DetailView):
    """
    Класс-представление страницы "Категория"
    """
    model = Category
    template_name = "apple_shop/category_detail.html"
    context_object_name = "category"

    def get_products_in_category(self):
        """
        Получение товаров категории для вывода на страницу
        """
        return Product.objects.filter(category=super().get_object())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["products"] = self.get_products_in_category()
        return context


def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Рендер страницы товара в интернет-магазине
    """
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "apple_shop/product_detail.html", context=context)


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "Контакты" приложения
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Получено сообщение '{message}' от пользователя {name} ({email})")
        return HttpResponse("Ваше сообщение успешно отправлено!")

    contact = ContactData.objects.get(id=1)
    context = {"contact": contact}

    return render(request, "apple_shop/contacts.html", context=context)


def owner(request: HttpRequest) -> HttpResponse:
    """
    Рендер страницы "Владелец" приложения
    """
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price_per_unit = request.POST.get("price_per_unit")
        category = request.POST.get("category")
        photo = request.FILES.get("photo")
        Product.objects.create(
            name=name,
            description=description,
            price_per_unit=price_per_unit,
            category=Category.objects.get(name=category),
            photo=photo
        )
        return HttpResponse("Новый товар успешно добавлен!")

    contact = ContactData.objects.get(id=1)
    context = {"contact": contact}

    return render(request, "apple_shop/owner.html", context=context)
