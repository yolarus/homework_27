from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import EMAIL_HOST_USER

from .forms import ArticleForm
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    """
    Класс-представление страницы "Главная"
    """
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """
    Класс-представление страницы "Статья"
    """
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        """
        Увеличение счетчика просмотров при рендере
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            send_mail(subject="Вы почти блогер!",
                      message="Поздравляем! Вы становитесь популярным!",
                      from_email=EMAIL_HOST_USER,
                      recipient_list=[EMAIL_HOST_USER])
        return self.object


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    Класс-представление для создания статьи
    """
    model = Article
    form_class = ArticleForm
    template_name = "blog/editor.html"
    success_url = reverse_lazy("blog:index")


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс-представление для обновления статьи
    """
    model = Article
    form_class = ArticleForm
    template_name = "blog/editor.html"
    success_url = reverse_lazy("blog:index")

    def get_success_url(self):
        """
        Перенаправление на страницу статьи
        """
        return reverse("blog:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс-представление для удаления статьи
    """
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:index")
