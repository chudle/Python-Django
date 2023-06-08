from django.db import models
from django.contrib.auth.models import User

class news (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "Заголовок")
    author = models.ForeignKey(User, null=True, verbose_name = "Автор", on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, verbose_name = "Тэг")
    text = models.TextField(blank=True, verbose_name = "Текст")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Время")
    is_published = models.BooleanField(default=True, verbose_name = "Опубликовано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
