from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
