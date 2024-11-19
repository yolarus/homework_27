from django.db import models


# Create your models here.
class Article(models.Model):
    """
    Модель статей блога для работы с БД
    """
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/articles/previews/",
                                verbose_name="Фото для превью",
                                blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(verbose_name="Статус", default=True)
    views_count = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return f"{self.title} от {self.created_at}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ['created_at']
