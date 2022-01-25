from django.db import models


class ArticleCategory(models.Model):
    title = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

