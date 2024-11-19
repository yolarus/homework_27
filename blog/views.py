from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article


# Create your views here.
class ArticleListView(ListView):
    """
    Класс-представление страницы "Блог"
    """
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
