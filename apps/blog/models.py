from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=150, unique=True)
    desciption = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title}'
