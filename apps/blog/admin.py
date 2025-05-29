from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'image',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = ('title', 'author',)
