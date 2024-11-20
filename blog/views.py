from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
