from django.urls import path

from blog.apps import BlogConfig

from . import views

app_name = BlogConfig.name

urlpatterns = [
    path("index/", views.ArticleListView.as_view(), name="index"),
    path("article/detail/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("owner/", views.ArticleCreateView.as_view(), name="owner"),
]
