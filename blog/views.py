from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


# Create your views here.
class ArticleListView(ListView):
    """
    Класс-представление страницы "Главная"
    """
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    """
    Класс-представление страницы "Статья"
    """
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"


class ArticleCreateView(CreateView):
    """
    Класс-представление для создания статьи
    """
    model = Article
    fields = ["title", "body", "preview"]
    template_name = "blog/editor.html"
    success_url = reverse_lazy("blog:index")


class ArticleUpdateView(UpdateView):
    """
    Класс-представление для обновления статьи
    """
    model = Article
    fields = ["title", "body", "preview"]
    template_name = "blog/editor.html"
    success_url = reverse_lazy("blog:index")


class ArticleDeleteView(DeleteView):
    """
    Класс-представление для удаления статьи
    """
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:index")
